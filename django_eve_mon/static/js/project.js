angular.module('djevemon', ['ui.bootstrap']);

var characterSelect = $('#select-characters');
var getCharsBtn = $('#btn-get-characters');
var addCharsBtn = $('#btn-add-characters');
var addCharForm = $('#add-character-form');

function AccordionDemoCtrl($scope) {
  $scope.oneAtATime = true;
}

function ajaxPostAddCharacterForm() {
  $.ajax({
    url: document.URL,
    type: 'POST',
    data: $(addCharForm).serialize(),
    success: function (result) {
      if (result.message === undefined) {
        $(characterSelect).select2({
          data: result.data,
          placeholder: "Select character(s)",
          multiple: true
        });
        $(characterSelect).select2('enable');
      } else {
        alert(result.message);
      }
      $(getCharsBtn).toggle();
      $(addCharsBtn).toggle();
    },
    error: function (data) {
      console.log(data);
    }
  }).always(function () {
    $(getCharsBtn).button('reset');
    $(addCharsBtn).button('reset');
  });
}

$(addCharsBtn).on('click', function () {
  $(addCharForm).submit();
//  $(addCharsBtn).button('loading');
//  ajaxPostAddCharacterForm();
});

$(getCharsBtn).on('click', function () {
  $(getCharsBtn).button('loading');
  ajaxPostAddCharacterForm();
});

$(document).ready(function(){
  $(characterSelect).select2({
    data: [{id: 1, text: 'foo'}],
    placeholder: "Select character(s)",
    multiple: true
  });
  $(characterSelect).select2('disable');
});
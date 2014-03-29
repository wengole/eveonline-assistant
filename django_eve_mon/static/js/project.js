angular.module('djevemon', ['ui.bootstrap']);

function AccordionDemoCtrl($scope) {
  $scope.oneAtATime = true;
}

var characterSelect = $('#select-characters');

var getCharsBtn = $('#btn-get-characters');
$(getCharsBtn).on('click', function () {
  $(getCharsBtn).button('loading');
  $.ajax({
    url: document.URL,
    type: 'POST',
    data: $('#add-character-form').serialize(),
    success: function (result) {
      console.log(result);
      $(characterSelect).select2({
        data: result.data,
        placeholder: "Select character(s)",
        multiple: true
      });
      $(characterSelect).select2('enable');
    },
    error: function (data) {
      console.log(data);
    }
  }).always(function () {
    $(getCharsBtn).button('reset')
  });
});

$(document).ready(function(){
  $(characterSelect).select2({
    data: [{id: 1, text: 'foo'}],
    placeholder: "Select character(s)",
    multiple: true
  });
  $(characterSelect).select2('disable');
});
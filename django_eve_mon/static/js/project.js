angular.module('djevemon', ['ui.bootstrap']);

function AccordionDemoCtrl($scope) {
  $scope.oneAtATime = true;
}

var getCharsBtn = $('#btn-get-characters');
$(getCharsBtn).on('click', function () {
  $(getCharsBtn).button('loading');
  $.ajax({
    url: document.URL,
    type: 'POST',
    data: $('#add-character-form').serialize(),
    success: function (result) {
      console.log(result);
    },
    error: function (data) {
      console.log(data);
    }
  }).always(function () {
    $(getCharsBtn).button('reset')
  });
});
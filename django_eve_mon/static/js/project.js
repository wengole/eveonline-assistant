angular.module('djevemon', ['ui.bootstrap']);

function AccordionDemoCtrl($scope) {
  $scope.oneAtATime = true;
}

var getCharsBtn = $('#btn-get-characters');
$(getCharsBtn).on('click', getCharacters($('#add-character-form'), $(getCharsBtn)));

function getCharacters(form, submitButton) {
  submitButton.button('loading');
  $.post(document.URL, form.serialize(), function (result) {
    alert(result);
  }, 'json').always(function () {
    submitButton.button('reset')
  });
}
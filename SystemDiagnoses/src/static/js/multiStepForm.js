function showStep(stepNumber) {
    // Get all fieldsets
    var fieldsets = document.querySelectorAll('.registration-form fieldset');

    // Remove 'active' class from all fieldsets
    for (var i = 0; i < fieldsets.length; i++) {
        fieldsets[i].classList.remove('active');
    }

    // Add 'active' class to the current fieldset
    var currentFieldset = document.querySelector('#step' + stepNumber);
    currentFieldset.classList.add('active');
}
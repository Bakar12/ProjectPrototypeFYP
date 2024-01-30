window.onload = function() {
    var form = document.querySelector('form');
    var modal = document.getElementById('confirmationModal');
    var span = document.getElementsByClassName('close')[0];

    form.onsubmit = function(event) {
        event.preventDefault();
        var formData = new FormData(form);
        var confirmationText = '';
        for (var pair of formData.entries()) {
            confirmationText += pair[0]+ ': ' + pair[1] + '\n';
        }
        document.getElementById('confirmationText').innerText = confirmationText;
        modal.style.display = 'block';
    }

    span.onclick = function() {
        modal.style.display = 'none';
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
}
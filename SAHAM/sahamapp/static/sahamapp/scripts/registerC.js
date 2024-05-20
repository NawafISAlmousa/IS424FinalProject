document.getElementById('registrationForm').addEventListener('submit', function(event) {
    const form = event.target;

    
    let isValid = true;
    form.querySelectorAll('input').forEach(input => {
        if (!input.checkValidity()) {
            isValid = false;
            input.reportValidity();
        }
    });

    if (!isValid) {
        event.preventDefault();
    }
});

document.querySelectorAll('input').forEach(input => {
    input.addEventListener('input', () => {
        input.setCustomValidity('');
    });
});
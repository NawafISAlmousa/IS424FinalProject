document.getElementById('registrationForm').addEventListener('submit', function(event) {
    const form = event.target;

    
    let isValid = true;
    form.querySelectorAll('input').forEach(input => {
        if (!input.checkValidity()) {
            isValid = false;
            // Show the custom validation message
            input.reportValidity();
        }
    });

    // If the form is invalid, prevent submission
    if (!isValid) {
        event.preventDefault();
    }
});

// Reset custom validity message when user starts typing again
document.querySelectorAll('input').forEach(input => {
    input.addEventListener('input', () => {
        input.setCustomValidity('');
    });
});
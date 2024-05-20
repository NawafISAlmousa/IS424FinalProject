    document.getElementById('editServiceForm').addEventListener('submit', function(event) {
        let serviceName = document.getElementById('serviceName').value;
        let serviceDescription = document.getElementById('serviceDescription').value;
        let price = document.getElementById('price').value;

        if (!serviceName || !serviceDescription || !price) {
            event.preventDefault();
            alert('Please fill out all required fields.');
        }
    });
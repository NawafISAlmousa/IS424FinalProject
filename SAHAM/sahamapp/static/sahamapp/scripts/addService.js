    document.getElementById('addServiceForm').addEventListener('submit', function(event) {
        var serviceName = document.getElementById('serviceName').value;
        var serviceDescription = document.getElementById('serviceDescription').value;
        var price = document.getElementById('price').value;

        if (!serviceName || !serviceDescription || !price) {
            event.preventDefault();
            alert('Please fill out all required fields.');
        }
    });
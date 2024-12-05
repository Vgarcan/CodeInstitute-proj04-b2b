document.getElementById('quantity').addEventListener('input', function() {
    // Gets the selected Quantity
    var quantity = document.getElementById('quantity').value;

    // Update the data-base-url with the new quantity
    var addToCartBtn = document.getElementById('addToCartBtn');
    var baseUrl = addToCartBtn.getAttribute('data-base-url');
    addToCartBtn.href = baseUrl.replace(/1$/, quantity);
});
document.addEventListener("DOMContentLoaded", () => {
    // General function to handle add or remove actions
    function handleCartAction(action, productId, quantityId, baseUrl) {
        document.getElementById(`${action}Link_${productId}`).addEventListener('click', function(event) {
            event.preventDefault();

            // Obtain an stoe the quantity
            var quantity = document.getElementById(`${quantityId}_${productId}`).value;

            // Update the URL with the quantity
            var updatedUrl = baseUrl.replace(/1$/, quantity);

            // Redirect to the updated URL
            window.location.href = updatedUrl;
        });
    }

    // Loop through cart items
    cartItems.forEach(item => {
        // Refactor 'remove' and 'add' actions
        handleCartAction(
            'remove',
            item.productId,
            'remove_quantity',
            item.removeUrl
        );

        handleCartAction(
            'add',
            item.productId,
            'add_quantity',
            item.addUrl
        );
    });
});
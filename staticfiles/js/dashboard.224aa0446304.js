// Update the URL in the update button
function updateStatusURL(orderId) {
    // Get the selected status from the dropdown
    const selectedStatus = document.getElementById(`actions-status-for-${orderId}`).value;
    // Get the button and the base URL from its data attribute
    const updateButton = document.getElementById(`update-button-${orderId}`);
    const baseURL = updateButton.getAttribute('data-url');
    // Update the button's href with the selected status
    updateButton.href = baseURL.replace('NEWSTATUS', selectedStatus);
}

// Button to load more orders
document.addEventListener("DOMContentLoaded", function() {
    if (!document.getElementById('no-data')) {
        let currentVisible = 20; // Initially show 20 rows
        const rows = document.querySelectorAll(".order-row, .recent-order-row");
        const loadMoreButton = document.getElementById("loadMore");

        loadMoreButton.addEventListener("click", function() {
            // Show 20 more rows on each button click
            for (let i = currentVisible; i < currentVisible + 20; i++) {
                if (rows[i]) {
                    rows[i].classList.remove("d-none");
                }
            }
            currentVisible += 20;

            // Hide the button if there are no more rows to show
            if (currentVisible >= rows.length) {
                loadMoreButton.style.display = "none";
            }
        });
    };

});
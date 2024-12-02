document.addEventListener('DOMContentLoaded',
    /**
     * This function initializes the responsive behavior of the navigation bar.
     * It adds a click event listener to the navbar toggler element, which toggles the collapse class on the navbar collapse element.
     *
     * @function
     * @returns {void}
     */
    function() {

        // UNDER DEV - Modal 
        // Show the modal automatically
        var modal = document.getElementById('developmentModal');
        var closeModalBtn = document.getElementById('closeModal');

        // Display the modal
        modal.style.display = 'block';

        // Close the modal when the button is clicked
        closeModalBtn.addEventListener('click', function() {
            modal.style.display = 'none';
        });
    });
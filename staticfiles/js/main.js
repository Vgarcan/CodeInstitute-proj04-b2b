document.addEventListener('DOMContentLoaded',
    /**
     * This function initializes the responsive behavior of the navigation bar.
     * It adds a click event listener to the navbar toggler element, which toggles the collapse class on the navbar collapse element.
     *
     * @function
     * @returns {void}
     */
    function() {
        /**
         * The navbar toggler element.
         * @type {HTMLElement}
         */
        const toggler = document.querySelector('.navbar-toggler');

        /**
         * The navbar collapse element.
         * @type {HTMLElement}
         */
        const navbarCollapse = document.querySelector('#navbarNav');

        toggler.addEventListener('click', function() {
            /**
             * Toggles the 'collapse' class on the navbar collapse element.
             */
            navbarCollapse.classList.toggle('collapse');
        });

        // BOOTSTRAP - Enable ToolTips
        // https://getbootstrap.com/docs/5.3/components/tooltips/#enable-tooltips
        const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
        const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

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
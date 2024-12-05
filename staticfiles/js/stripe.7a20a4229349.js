// Access Stripe configuration from the global variable
document.addEventListener('DOMContentLoaded', function() {
    // Ensure configuration is available
    const stripeConfig = window.stripeConfig || {};
    const publicKey = stripeConfig.publicKey;
    const clientSecret = stripeConfig.clientSecret;
    const placeOrderUrl = stripeConfig.placeOrderUrl;
    const confirmOrderUrl = stripeConfig.confirmOrderUrl;
    const csrfToken = stripeConfig.csrfToken;

    if (!publicKey || !clientSecret) {
        console.error('Stripe configuration is missing.');
        return;
    }

    // Initialise Stripe with the public key
    const stripe = Stripe(publicKey);
    const elements = stripe.elements();

    // Customise the appearance of the card Element
    const style = {
        base: {
            color: '#32325d',
            fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
            fontSmoothing: 'antialiased',
            fontSize: '16px',
            '::placeholder': {
                color: '#aab7c4',
            },
        },
        invalid: {
            color: '#fa755a',
            iconColor: '#fa755a',
        },
    };

    // Create an instance of the card Element and mount it
    const card = elements.create('card', {
        style: style,
        hidePostalCode: true,
    });
    card.mount('#card-element');

    // Handle real-time validation errors from the card Element
    card.on('change', function(event) {
        const displayError = document.getElementById('card-errors');
        displayError.textContent = event.error ? event.error.message : '';
    });

    /**
     * Validates the required form fields to ensure no empty values are submitted.
     * Highlights fields with errors and provides visual feedback.
     */
    function validateForm(activeForm, requiredFields, phoneId, emailId) {
        let isValid = true;

        requiredFields.forEach((fieldId) => {
            const field = document.getElementById(fieldId);

            if (!field || !field.value.trim()) {
                // Highlight field with error using Bootstrap's is-invalid class
                field.classList.add('is-invalid');
                isValid = false;
            } else {
                // Remove error highlight if the field is valid
                field.classList.remove('is-invalid');
            }
        });

        // Specific validation for phoneId to ensure it's an integer
        const phoneField = document.getElementById(phoneId);
        if (phoneField && !/^\d+$/.test(phoneField.value.trim())) {
            phoneField.classList.add('is-invalid');
            document.getElementById('card-errors').textContent =
                'Phone number must contain only numbers.';
            isValid = false;
        } else if (phoneField) {
            phoneField.classList.remove('is-invalid');
        }

        // Specific validation for emailId to ensure it's a valid email
        const emailField = document.getElementById(emailId);
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email validation regex
        if (emailField && !emailPattern.test(emailField.value.trim())) {
            emailField.classList.add('is-invalid');
            document.getElementById('card-errors').textContent =
                'Please enter a valid email address.';
            isValid = false;
        } else if (emailField) {
            emailField.classList.remove('is-invalid');
        }

        return isValid;
    }

    // Function to confirm payment for the active form
    function confirmPayment(
        activeForm,
        nameId,
        emailId,
        phoneId,
        addressId,
        cityId,
        countryId,
        postalCodeId
    ) {
        // Validate the form before processing payment
        const requiredFields = [
            nameId,
            emailId,
            phoneId,
            addressId,
            cityId,
            countryId,
            postalCodeId,
        ];
        if (!validateForm(activeForm, requiredFields, phoneId, emailId)) {
            document.getElementById('card-errors').textContent =
                'Please correct the errors in the form.';
            return;
        }

        const formData = new FormData(activeForm);
        console.log([...formData]);
        console.log('Billing Name:', document.getElementById(nameId).value);
        console.log('Billing Email:', document.getElementById(emailId).value);
        console.log('Billing Phone:', document.getElementById(phoneId).value);
        console.log('Billing Address:', document.getElementById(addressId).value);
        console.log('Billing City:', document.getElementById(cityId).value);
        console.log('Billing Country:', document.getElementById(countryId).value);
        console.log('Billing Postal Code:', document.getElementById(postalCodeId).value);

        // Disable the submit button to prevent multiple submissions
        const submitButton = document.getElementById('submit-button');
        submitButton.disabled = true;
        submitButton.textContent = 'Processing...';

        // Perform a stripe payment request
        stripe
            .confirmCardPayment(clientSecret, {
                payment_method: {
                    card: card,
                    billing_details: {
                        name: document.getElementById(nameId).value,
                        email: document.getElementById(emailId).value,
                        phone: document.getElementById(phoneId).value,
                        address: {
                            line1: document.getElementById(addressId).value,
                            city: document.getElementById(cityId).value,
                            country: document.getElementById(countryId).value,
                            postal_code: document.getElementById(postalCodeId).value,
                        },
                    },
                },
            })
            .then(function(result) {
                if (result.error) {
                    // Show Stripe error message
                    document.getElementById('card-errors').textContent =
                        result.error.message;
                    // Re-enable the submit button if there's an error
                    submitButton.disabled = false;
                    submitButton.textContent = 'Pay';
                } else if (result.paymentIntent.status === 'succeeded') {
                    // Add CSRF token and submit form data via fetch
                    fetch(placeOrderUrl, {
                            method: 'POST',
                            body: formData,
                            headers: { 'X-CSRFToken': csrfToken },
                        })
                        .then((response) => {
                            if (response.ok) {
                                console.log('Redirecting to confirmation page...');
                                window.location.href =
                                    confirmOrderUrl;
                            } else {
                                console.error('Server Error:', response);
                                document.getElementById('card-errors').textContent =
                                    'An error occurred. Please try again.';
                                submitButton.disabled = false;
                                submitButton.textContent = 'Pay';
                            }
                        })
                        .catch((error) => {
                            console.error('Network Error:', error);
                            document.getElementById('card-errors').textContent =
                                'A network error occurred. Please try again.';
                            submitButton.disabled = false;
                            submitButton.textContent = 'Pay';
                        });
                }
            });
    }

    // Event handler for the Pay button
    document
        .getElementById('submit-button')
        .addEventListener('click', function(event) {
            event.preventDefault();
            // Check the active tab and set the appropriate form
            const activeTab = document.querySelector('.tab-pane.active');
            if (activeTab && activeTab.id === 'profile') {
                confirmPayment(
                    document.getElementById('payment-form'),
                    'full-name',
                    'email',
                    'phone-number',
                    'address',
                    'city',
                    'country',
                    'postal-code'
                );
            } else {
                confirmPayment(
                    document.getElementById('alt-payment-form'),
                    'alt-full-name',
                    'alt-email',
                    'alt-phone-number',
                    'alt-address',
                    'alt-city',
                    'alt-country',
                    'alt-postal-code'
                );
            }
        });
});
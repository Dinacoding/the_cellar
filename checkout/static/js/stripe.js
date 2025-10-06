// Get the public key and client secret passed from the Django view
const stripePublicKey = document.getElementById('id_stripe_public_key').textContent.slice(1, -1);
const clientSecret = document.getElementById('id_client_secret').textContent.slice(1, -1);
const form = document.getElementById('payment-form');
const submitButton = document.getElementById('submit-button');


const stripe = Stripe(stripePublicKey);

const elements = stripe.elements({
    clientSecret: clientSecret,
    appearance: {
        theme: 'stripe',
        variables: {
            fontSizeBase: '16px',
            colorText: '#32325d',
            colorDanger: '#fa755a',
            fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
        },
    }
});

const paymentElement = elements.create('payment');
paymentElement.mount('#payment-element');

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    
    // Disable the button while processing
    submitButton.disabled = true;

    const { error } = await stripe.confirmPayment({
        elements,
        confirmParams: {
            // We use the current page URL as the base.
            return_url: window.location.href, 
        },
        redirect: 'if_required', 
    });

    if (error) {
        const errorDiv = document.getElementById('card-errors');
        errorDiv.textContent = error.message;
    } else {
        // The payment has been processed successfully by Stripe.
        // Now, submit the non-Stripe form data (address, phone, etc.) to your Django view.
        form.submit();
    }
});
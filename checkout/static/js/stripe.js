/**
 * Example: Create a Stripe instance and handle payment form submission.
 * Replace 'your-publishable-key' with your actual Stripe publishable key.
 */

// Load Stripe.js (make sure to include Stripe.js in your HTML file)
// <script src="https://js.stripe.com/v3/"></script>

const stripe = Stripe('pk_test_51S9Bc9F7CPMer9VbvHRHuZ8oKV7yyrBV7HAJDqXZpqPFM62X05bUvTdQa0R7m8IfmgB3vS8yvNeg2zKye0XY4WLz00cHe0DaQT');
// Example function to handle payment form submission
async function handlePayment(event) {
    event.preventDefault();

    const elements = stripe.elements();
    const card = elements.create('card');
    card.mount('#card-element');

    const {error, paymentMethod} = await stripe.createPaymentMethod({
        type: 'card',
        card: card,
    });

    if (error) {
        console.error(error.message);
        // Display error to user
    } else {
        console.log('PaymentMethod created:', paymentMethod);
        // Send paymentMethod.id to your server for further processing
    }
}

// Example: Attach handler to a form
document.getElementById('payment-form').addEventListener('submit', handlePayment);
<<<<<<< HEAD
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe('pk_test_51S9Bc9F7CPMer9VbvHRHuZ8oKV7yyrBV7HAJDqXZpqPFM62X05bUvTdQa0R7m8IfmgB3vS8yvNeg2zKye0XY4WLz00cHe0DaQT');
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
=======
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
>>>>>>> adf4a1a0602751fa3a9cd0bef8c6403824cd0678
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';        
    }
});
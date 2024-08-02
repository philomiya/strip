from flask import Flask, render_template, jsonify, request
import stripe

app = Flask(__name__)

# Set your secret key here
stripe.api_key = 'sk_test_51PirhhE51PBQdkHirs8lXJgbu1v5JWZ6DBsQMqIMjRgk9R9RjmleKzX1Isuvcvfjm21FyB4a5SWCaxfknscVoRTv00YwuozY3I'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'T-shirt',
                    },
                    'unit_amount': 2000,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.host_url + 'success',
            cancel_url=request.host_url + 'cancel',
        )
        return jsonify({'id': session.id})
    except Exception as e:
        return jsonify(error=str(e)), 403

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/cancel')
def cancel():
    return render_template('cancel.html')

if __name__ == '__main__':
    app.run(port=4242)

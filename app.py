from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Sample product data (you can replace it with your own database)
products = [
    {"id": 1, "name": "Product 1", "price": 50, "image": "shoe1.jpg"},
    {"id": 2, "name": "Product 2", "price": 60, "image": "shoe2.jpg"},
    {"id": 3, "name": "Product 3", "price": 70, "image": "shoe3.jpg"}
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        if 'cart' not in session:
            session['cart'] = []
        session['cart'].append(product)
        return redirect(url_for('index'))
    else:
        return "Product not found", 404

@app.route('/cart')
def view_cart():
    cart = session.get('cart', [])
    total_price = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total_price=total_price)

@app.route('/checkout')
def checkout():
    session.pop('cart', None)
    return "Checkout successful!"

if __name__ == '__main__':
    app.run(debug=True)

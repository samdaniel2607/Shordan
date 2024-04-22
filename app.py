from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def index():
    return render_template('signup.html')

@app.route('/login')
def index():
    return render_template('login.html')

@app.route('/shoedetails')
def index():
    return render_template('shoedetails.html')
@app.route('/shop')
def index():
    return render_template('shop.html')

if __name__ == '__main__':
    app.run(debug=True)

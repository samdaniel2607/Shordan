from flask import flask, render_template
request session
app=flask(__name__)
@app.route("/") #default
def login():
    return render_template("login.html")
@app route ("/signup")
def signup():
    return render_templates("signup.html")
if __name__ == "__main__":
    app.run(debug=True)
    Python app.py
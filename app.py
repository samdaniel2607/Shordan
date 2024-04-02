from flask import Flask, render_template

app=Flask(__name__)


@app.route("/") #default
def login():
    return render_template("index.html")

#@app route ("/signup")
 # def signup():
  #  return render_templates("signup.html")

#changed
if __name__ == "__main__":
    app.run(debug=True)
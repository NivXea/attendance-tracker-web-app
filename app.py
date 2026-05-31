from flask import Flask, render_template , request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "MySecretKey"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contact-us")
def contact():
    return "Contact Us!"

@app.route("/login")
def login():
    return render_template("login.html")   

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/verify-login", methods=["POST"])
def verify_user():
    name = request.form['username']
    password = request.form['password']
    return f"Thank you for logging in: {name}."

if __name__ == "__main__":
    app.run(debug=True)




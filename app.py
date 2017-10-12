from flask import Flask, render_template, request, session, redirect, url_for, flash
username = "un"
password = "pw"

my_app = Flask(__name__)
my_app.secret_key = 'who cares about security'

@my_app.route('/')
def root():
    if session.has_key("username"):
        return redirect(url_for('welcome'))
    return redirect(url_for("login"))
  
@my_app.route("/login", methods=["POST","GET"])
def login():
    return render_template("login.html")

@my_app.route("/auth", methods=["POST","GET"])
def auth():
    if(request.form["username"]!="un"):
        flash("wrong username")
        return redirect(url_for("login"))
    elif(request.form["password"]!="pw"):
        flash("wrong password")
        return redirect(url_for("login"))
    else:
        session["username"]=request.form["username"]
        session['password'] = request.form['password']
        return redirect(url_for('welcome'))

@my_app.route("/welcome", methods=["POST","GET"])
def welcome():
    return render_template("welcome.html",username=session["username"])

@my_app.route("/logout", methods=["POST"])
def logout():
    session.pop("username")
    session.pop("password")
    return redirect(url_for("login"))

if __name__ == "__main__":
    my_app.debug = True
    my_app.run()

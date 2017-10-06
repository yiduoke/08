from flask import Flask, render_template, request, session
username = "un"
password = "pw"

my_app = Flask(__name__)
my_app.secret_key = 'who cares about security'

@my_app.route('/')
def root():
    if session.has_key("username"):
        return render_template("loggedin.html", username = session["username"])
    return render_template("login.html")
  
@my_app.route("/login", methods=["POST"])
def login():
    if (request.form["username"]=="un" and request.form["password"]=="pw"):
        session["username"]=request.form["username"]
        session['password'] = request.form['password']
        return render_template("loggedin.html",username=request.form["username"])
    elif (request.form["username"]!="un"):
        return render_template("error.html",errorMessage="wrong username")
    else:
        return render_template("error.html",errorMessage="wrong password")

# @my_app.route("/loggedin", methods=["POST"])
# def loggedin():
#     return render_template("loggedin.html",username=session["username"])

@my_app.route("/logout", methods=["POST"])
def logout():
    session.pop("username")
    session.pop("password")
    return render_template("login.html")

if __name__ == "__main__":
    my_app.debug = True
    my_app.run()

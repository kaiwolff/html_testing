from flask import Flask, request, abort, render_template


def check_login(username,password):
    if username == "test" and password == "test":
        return True

    elif username == "admin" and password == "admin":
        return True

    else:
        return False

def attempt_register(username, password, firstname, lastname, birthyear):
    if username == "test" and password == "safe":
        return "Congratulations {}, you have succesfully registered. You may now log in".format(username)
    elif username == "taken":
        return "Username {} is already taken".format(username)
    elif password != "safe":
        return "Password insecure, please try again"
    else:
        return "Unknown Error"


def check_manager(username, password):
    validate = check_login(username, password)
    if username == "admin" and validate == True:
        return True

    else:
        return False




app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    #run register attempt
    firstname = request.form.get('firstname', type=str)
    lastname = request.form.get('lastname', type=str)
    birthyear = request.form.get('birthyear', type=str)
    password = request.form.get('password', type=str)
    username = request.form.get('username', type=str)

    message = attempt_register(username, password, firstname, lastname, birthyear)
    #now have the message returned by the attempt_register function

    return render_template("register.html", message = message)



@app.route('/login', methods=['GET', 'POST'])

def attempt_login():
    #run loging attempt
    username = request.form.get('username', type=str)
    password = request.form.get('password', type=str)


    if check_login(username,password) == True:
        if check_manager(username, password) == True:
            return render_template('manager_options.html')
        return render_template('logged_in.html', username = username)

    else:
        abort(403)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

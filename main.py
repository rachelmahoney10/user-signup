from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 

def vaild_check(word, t):
    if t == "username":
        for l in word:
            if l == " ":
                return False
            else:
                return True
    if len(word) >= 3 and len(word) <= 20:
        return True
    else:
        return False

@app.route('/')
def index():
    return render_template('form.html')

@app.route("/", methods=['POST'])
def handle_form():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
    username_error = password_error = verify_password_error = email_error = ''

    if username == '' or vaild_check(username, username) == False:
        username_error = "That's not a valid username"
    
    if password == '' or vaild_check(password, password) == False:
        password_error = "That's not a vaild password"

    if verify_password == '' or vaild_check(verify_password, password) == False or password != verify_password:
        verify_password_error = "Passwords don't match"

    at_count = 0
    period_count = 0

    for l in email:
        if l == '@':
            at_count = at_count + 1
        elif l == '.':
            period_count = period_count + 1
        if l == ' ':
            email_error = "That is not a valid email"
            break

    if at_count != 1 or period_count != 1:
        email_error = "That is not a valid email"

    if username_error == '' and password_error == '' and verify_password_error == '' and email_error == '':
        return render_template('signup.html', username=username)
    else:
        return render_template('form.html', username_error=username_error, username=username, password_error=password_error, verify_password_error=verify_password_error, email_error=email_error, email=email)

    
app.run()
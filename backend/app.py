import os
import psycopg2
from flask import Flask, render_template 
from flask import Flask, render_template, request, url_for, redirect
from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager



app= Flask(__name__)
csrf = CSRFProtect(app)
csrf.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


# set this in env
app.secret_key = b''



@app.route('/create/', methods=('GET', 'POST'))
def create():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'
    return render_template('create.html')

@app.route('/home', methods=('GET'))
def home():
    return render_template('home.html')

@app.route('/edit',methods=('PUT'))
def edit():
    return render_template('update.html')

@app.route('/remove', methods=('DELETE'))
def delete():
    return render_template('delete.html')

@app.route('/login',methods=('GET', 'POST'))
def login():
    # if request.method == 'POST':
    #     session['username'] = request.form['username']
    #     return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        Flask.flash('Logged in successfully.')

        next = Flask.request.args.get('next')
        # url_has_allowed_host_and_scheme should check if the url is safe
        # for redirects, meaning it matches the request host.
        # See Django's url_has_allowed_host_and_scheme for an example.
        if not url_has_allowed_host_and_scheme(next, request.host):
            return Flask.abort(400)

        return Flask.redirect(next or flask.url_for('index'))
    
    return Flask.render_template('login.html', form=form)
    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
# jwt 

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
        is_auth=True
        is_active=True 
    

    def __str__(self):
        return "User(id='%s')" % self.id


users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app, authenticate, identity)

@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity

if __name__ == '__main__':
    app.run(debug=True)
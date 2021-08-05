from flask import Blueprint, render_template, redirect, url_for, request, flash, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)

...
@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    login_user(user, remember=remember)
    # if the above check passes, then we know the user has the right credentials
    return redirect(url_for('main.home'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

    
@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    is_vendor = request.form.get('is_vendor')
    is_cashier = request.form.get('is_cashier')

    MASTER = {"CapitaLand" : "GRWzj1RD3lvtDsTJ", 
    "Far East Organisation": "0sTApeqt4oTm9ojv", 
    "Frasers Property": "NkriYNQ7JamPNRw7", 
    "Mapletree": "5LbjNfJzr3fKqPJS"}

    if (not is_vendor) and (not is_cashier):
        identity = "customer" # Convert empty string to Customer
        company = ""
    elif is_cashier:
        identity = "cashier"
        company = ""
    else:
        identity = "vendor"
        company = request.form.get('company')
        code = request.form.get('code')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user:
        flash('Email address already exists') # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for('auth.signup'))

    if identity == "vendor":
        if MASTER[company] != code:
            flash('Invalid Secret Code') # If the user enters the wrong Secret Code for vendor account, redirect back to signup page to try again
            return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'), identity=identity, company = company)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))


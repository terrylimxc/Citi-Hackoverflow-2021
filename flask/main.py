from flask import Blueprint, render_template
from . import db
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('signup.html')

@main.route('/main')
@login_required
def home():
    if current_user.identity == "Vendor":
        return render_template('vendor.html',name=current_user.name)
    else:
        return render_template('customer_home.html',name=current_user.name)

@main.route('/main/buy')
@login_required
def buy():
    return render_template('customer_buy.html')

@main.route('/main/wallet')
@login_required
def wallet():
    return render_template('customer_wallet.html')
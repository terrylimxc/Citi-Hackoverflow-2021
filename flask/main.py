from flask import Blueprint, render_template, redirect, request
from . import db
from .models import User, Voucher
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('signup.html')

@main.route('/main')
@login_required
def home():
    if current_user.identity == "vendor":
        return redirect('/seller')
    elif current_user.identity == "cashier":
        return redirect('/cashier')
    else:
        return redirect('/buyer')


###############################
#                             #
#            Buyer            #
#                             #
###############################
@main.route('/buyer')
@login_required
def buyer_home():
    return render_template('customer_home.html', name=current_user.name)

@main.route('/buyer/buy')
@login_required
def buy():
    return render_template('customer_buy.html')

@main.route('/buyer/wallet')
@login_required
def buyer_wallet():
    return render_template('customer_wallet.html')

@main.route('/buyer/checkout')
@login_required
def checkout():
    return render_template('customer_checkout.html')


################################
#                              #
#            Seller            #
#                              #
################################
@main.route('/seller')
@login_required
def seller_home():
    all_vouchers = Voucher.query.filter_by(company=current_user.company).order_by(Voucher.denomination, Voucher.price).all()

    return render_template('vendor_home.html', name=current_user.name, all_vouchers=all_vouchers)

@main.route('/seller/sell')
@login_required
def sell():
    return render_template('vendor_sell.html', company=current_user.company)


@main.route('/seller/sell', methods=['POST'])
@login_required
def sell_post():
    voucher_type = int(request.form.get('voucher_type'))
    price = float(request.form.get('price'))
    quantity = int(request.form.get('quantity'))

    voucher = Voucher.query.filter_by(company=current_user.company, denomination=voucher_type).all()

    if not voucher: # check if there is a record of the voucher
        new_voucher = Voucher(company=current_user.company, denomination=voucher_type, price=price, quantity=quantity)
        db.session.add(new_voucher)
        db.session.commit()
        return render_template('vendor_sell_add.html', company=current_user.company, voucher_type=voucher_type, price=price, quantity=quantity)
    else:
        # check if a similar type of voucher exist in the Database
        voucher_2 = Voucher.query.filter_by(company=current_user.company, denomination=voucher_type, price=price).first()

        if not voucher_2: # Particular price not in Database -> create new record
            new_voucher = Voucher(company=current_user.company, denomination=voucher_type, price=price, quantity=quantity)
            db.session.add(new_voucher)
            db.session.commit()
            return render_template('vendor_sell_add.html', company=current_user.company, voucher_type=voucher_type, price=price, quantity=quantity)

        else: # Particular price in Database -> Update quantity of record
            voucher_2.quantity = quantity
            db.session.commit()
            return render_template('vendor_sell_update.html', company=current_user.company, voucher_type=voucher_type, price=price, quantity=quantity)


#################################
#                               #
#            Cashier            #
#                               #
#################################
@main.route('/cashier')
@login_required
def cashier_home():
    return render_template('cashier_home.html', name=current_user.name)
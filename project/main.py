from flask import Blueprint, render_template, redirect, request
from . import db
from .models import User, Voucher, LoyaltyPoints, User_Voucher, Cart
from flask_login import login_required, current_user
from flask_qrcode import QRcode


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
    user_points = LoyaltyPoints.query.filter_by(username=current_user.email).first()
    user_vouchers = User_Voucher.query.filter_by(username=current_user.email).all()

    if not user_points:
        user_points = 0
    else:
        user_points = user_points.points

    if not user_vouchers:
        user_vouchers = 0
    else:
        y = 0
        for i in user_vouchers:
            y += i.quantity
        user_vouchers = y

    return render_template('customer_home.html', name=current_user.name, points=user_points, vouchers=user_vouchers)

@main.route('/buyer/buy')
@login_required
def buy():
    all_vouchers = Voucher.query.order_by(Voucher.company, Voucher.denomination, Voucher.price).all()
    all_companies = [company.company for company in Voucher.query.with_entities(Voucher.company).distinct()]
    all_companies.insert(0, "All")

    return render_template('customer_buy.html', all_vouchers=all_vouchers, all_companies=all_companies)

@main.route('/buyer/buy', methods=['POST'])
@login_required
def buy_post():
    selected_company = request.form.get('filter_company')
    selected_company = " ".join(selected_company.split("+"))
    if selected_company != "All":
        all_vouchers = Voucher.query.filter_by(company=selected_company).order_by(Voucher.denomination, Voucher.price).all()
        temp = [company.company for company in Voucher.query.with_entities(Voucher.company).distinct()]
        temp.remove(selected_company)

        all_companies = [selected_company, "All"]
        all_companies.extend(temp)

    else:
        all_vouchers = Voucher.query.order_by(Voucher.company, Voucher.denomination, Voucher.price).all()
        all_companies = [company.company for company in Voucher.query.with_entities(Voucher.company).distinct()]
        all_companies.insert(0, "All")

    return render_template('customer_buy.html', all_vouchers=all_vouchers, all_companies=all_companies)

@main.route('/buyer/add', methods=['POST'])
@login_required
def add_post():
    value = request.form['Add Button']
    denomination, company, price = value.split("+")

    item = Cart.query.filter_by(company=company, denomination=denomination, price=price).all()

    if not item: # check if there is a record of the item
        new_item = Cart(company=company, denomination=denomination, price=price, quantity=1)
        db.session.add(new_item)
        db.session.commit()
    else:
        new_item = Cart.query.filter_by(company=company, denomination=denomination, price=price).first()
        new_item.quantity += 1
        db.session.commit()

    all_vouchers = Voucher.query.order_by(Voucher.company, Voucher.denomination, Voucher.price).all()
    all_companies = [company.company for company in Voucher.query.with_entities(Voucher.company).distinct()]
    all_companies.insert(0, "All")

    return render_template('customer_buy.html', all_vouchers=all_vouchers, all_companies=all_companies)


@main.route('/buyer/wallet')
@login_required
def buyer_wallet():
    current_items = User_Voucher.query.order_by(User_Voucher.company, User_Voucher.denomination).all()
    seq = list(range(1, len(current_items)+1))
    current_items = list(zip(seq, current_items))
    return render_template('customer_wallet.html', current_items=current_items)

@main.route('/buyer/wallet', methods=['POST'])
@login_required
def buyer_wallet_post():
    value = request.form['Use Button']
    company, denomination = value.split("+")
    text = "_".join([current_user.email, company, denomination])

    voucher = "${} {} Voucher".format(denomination, company)

    item = User_Voucher.query.filter_by(username=current_user.email, company=company, voucher=voucher, denomination=denomination).first()

    item.quantity -= 1

    if item.quantity == 0:
        User_Voucher.query.filter_by(username=current_user.email, company=company, voucher=voucher, denomination=denomination).delete()
    db.session.commit()

    return render_template('customer_wallet_use.html', text=text)

@main.route('/buyer/checkout')
@login_required
def checkout():
    all_items = Cart.query.order_by(Cart.company, Cart.denomination, Cart.price).all()
    return render_template('customer_checkout.html', all_items=all_items)

@main.route('/buyer/checkout', methods=['POST'])
@login_required
def checkout_post():
    all_items = Cart.query.all()

    for i in all_items:
        company, voucher, denomination, price, quantity = i.company, "${} {} Voucher".format(i.denomination, i.company), i.denomination, i.price, i.quantity

        x = User_Voucher.query.filter_by(username=current_user.email, company=company, voucher=voucher, denomination=denomination).first()

        if not x:
            new_voucher = User_Voucher(username=current_user.email, company=company, voucher=voucher, denomination=denomination, quantity=quantity)

            db.session.add(new_voucher)
        else:
            x.quantity += quantity
    
        stock = Voucher.query.filter_by(company=company, denomination=denomination, price=price).first()
        stock.quantity -= quantity

        loyalty = LoyaltyPoints.query.filter_by(username=current_user.email).first()
        points = int(10 * price)
        if not loyalty:
            new_loyalty = LoyaltyPoints(username=current_user.email, points=points)
            db.session.add(new_loyalty)
        else:
            loyalty.points += points
        
        db.session.query(Cart).delete()
        db.session.commit()

    return redirect('/buyer/wallet')


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
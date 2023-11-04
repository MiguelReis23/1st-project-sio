from flask import Blueprint, render_template, redirect, url_for, request, flash, Flask
from flask_login import login_required, current_user    
from .models import User
from .models import Product
from .models import Cart


from . import db
import os


crt= Blueprint('cart', __name__)

@crt.route('/cart', methods=['GET'])
@login_required
def cart():
    user=User.query.filter_by(id=current_user.id).first()
    cart = Cart.query.filter_by(user_id=current_user.id).all()
    product_details = [ Product.query.filter_by(id=cart_item.product_id).first() for cart_item in cart ]

    print("---------")
    print(product_details)
    print("---------")
    for product in product_details:
        print(product.image)
    return render_template('cart.html', user=user, product_details=product_details)


@crt.route('/cart/add/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    product=Product.query.get(product_id)
    if product:
        cart_item = Cart.query.filter_by(user_id=current_user.id, product_id=product_id).first()
        if cart_item:
            flash("Item already in cart")
        else:
            cart_item = Cart(user_id=current_user.id, product_id=product_id)
            db.session.add(cart_item)
            print("---------")
            flash("item added to cart")
            print("---------")
        db.session.commit()
        

    return redirect(url_for('main.index'))


@crt.route('/cart/remove/<int:product_id>', methods=['POST'])
@login_required
def remove_from_cart(product_id):
    product=Product.query.get(product_id)
    if product:
        cart_item = Cart.query.filter_by(user_id=current_user.id, product_id=product_id).first()
        if cart_item:
            db.session.delete(cart_item)
        db.session.commit()
        print("---------")
        flash("item removed from cart")
        print("---------")

    return redirect(url_for('cart.cart'))



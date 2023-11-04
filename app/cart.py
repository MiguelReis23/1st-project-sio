from flask import Blueprint, render_template, redirect, url_for, request, flash, Flask
from flask_login import login_required, current_user    
from .models import User
from .models import Product
from .models import Cart
from .models import CartItem


from . import db
import os


crt= Blueprint('cart', __name__)

@crt.route('/cart')
@login_required
def cart():
    user = User.query.filter_by(id=current_user.id).first()	
    if user.cart_id is None:
        cart = Cart(user_id=current_user.id)
        db.session.add(cart)
        db.session.commit()
        user.cart_id = cart.id
        db.session.commit()
    else:
        cart = Cart.query.filter_by(id=user.cart_id).first()
    cart_items = CartItem.query.filter_by(cart_id=cart.id).all()
    print("---------")
    print(cart)
    print("---------")
    print(cart_items)
    print("---------")
    return render_template('cart.html', user=user)

@crt.route('/cart/add/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    user = User.query.filter_by(id=current_user.id).first()
    cart = Cart.query.filter_by(id=user.cart_id).first()
    cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()
    if cart_item is None:
        cart_item = CartItem(cart_id=cart.id, product_id=product_id)
        db.session.add(cart_item)
    else:
        cart_item.quantity += 1
    db.session.commit()
    return redirect(url_for('cart.cart'))

@crt.route('/cart/remove/<int:product_id>', methods=['POST'])
@login_required
def remove_from_cart(product_id):
    user = User.query.filter_by(id=current_user.id).first()
    cart = Cart.query.filter_by(id=user.cart_id).first()
    cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()
    if cart_item.quantity == 1:
        db.session.delete(cart_item)
    else:
        cart_item.quantity -= 1
    db.session.commit()
    return redirect(url_for('cart.cart'))






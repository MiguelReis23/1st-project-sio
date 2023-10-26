from flask import Blueprint, render_template, redirect, url_for, request, flash, Flask
from flask_login import login_required, current_user    
from .models import User
from .models import Product

from . import db
import os


crt= Blueprint('cart', __name__)

@crt.route('/cart')
@login_required
def cart():
    user = User.query.filter_by(id=current_user.id).first()	
    return render_template('cart.html', user=user)

@crt.route('/cart/add/<int:product_id>', methods=['GET', 'POST'])
@login_required
def add_to_cart(product_id):
    user = User.query.filter_by(id=current_user.id).first()
    product = Product.query.filter_by(id=product_id).first()
    if product.has_stock:
        cart = Cart(user_id=user.id, product_id=product.id)
        db.session.add(cart)
        db.session.commit()
        flash('Product added to cart!', 'success')
    else:
        flash('Product is out of stock!', 'danger')
    return redirect(url_for('main.home'))

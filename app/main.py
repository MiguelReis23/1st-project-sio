from flask import Blueprint, render_template
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, Product, Category, Cart, CartItem, Review, Wishlist
main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
@login_required
def index():
    user=User.query.filter_by(id=current_user.id).first()
    products = Product.query.all()
    return render_template('index.html',user=user, products=products)


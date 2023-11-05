from flask import Blueprint, render_template, redirect, url_for, request, flash, Flask
from flask_login import login_required, current_user    
from .models import User, Wishlist, Product, Category
from . import db
from flask import jsonify
import os

src= Blueprint('search', __name__)


@src.route('/search', methods=['GET'])
@login_required
def search():
    return render_template('search.html')



@src.route('/search/products', methods=['GET'])
@login_required
def search_products():
    query = request.args.get('search')
    results={"query": query, "results": []}
    products = Product.query.filter(Product.name.contains(query)).all()
    for product in products:
        results["results"].append({"name": product.name, "price": product.price, "id": product.id, "image": product.image, "description": product.description})
    print(results)
    return jsonify(results)


from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(200), nullable=False)

@app.route('/customer', methods=['POST'])
def add_customer():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    customer = Customer(name=name, email=email, password=password)
    db.session.add(customer)
    db.session.commit()
    return jsonify({'message': 'Customer added successfully'})

@app.route('/user', methods=['POST'])
def add_user():
    username = request.json['username']
    password = request.json['password']
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User added successfully'})

@app.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    price = request.json['price']
    product = Product(name=name, price=price)
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product added successfully'})

@app.route('/order', methods=['POST'])
def add_order():
    customer_id = request.json['customer_id']
    product_id = request.json['product_id']
    quantity = request.json['quantity']
    order = Order(customer_id=customer_id, product_id=product_id, quantity=quantity)
    db.session.add(order)
    db.session.commit()
    return jsonify({'message': 'Order added successfully'})

@app.route('/payment', methods=['POST'])
def add_payment():
    customer_id = request.json['customer_id']
    amount = request.json['amount']
    payment = Payment(customer_id=customer_id, amount=amount)
    db.session.add(payment)
    db.session.commit()
    return jsonify({'message': 'Payment added successfully'})

@app.route('/review', methods=['POST'])
def add_review():
    customer_id = request.json['customer_id']
    product_id = request.json['product_id']
    rating = request.json['rating']
    comment = request.json['comment']
    review = Review(customer_id=customer_id, product_id=product_id, rating=rating, comment=comment)
    db.session.add(review)
    db.session.commit()
    return jsonify({'message': 'Review added successfully'})

if __name__ == '__main__':
    app.run(debug=True)

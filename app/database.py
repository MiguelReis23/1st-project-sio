from flask import Blueprint,jsonify
from app import db
from app.models import User
from app.models import Product
from app.models import Category

database = Blueprint('database', __name__)

@database.route('/generate', methods=['GET'])
def create_db():
    db.create_all()
    return jsonify({'message': 'Database created successfully!'}), 200

@database.route('/generate/users', methods=['GET'])
def create_users():
    db.session.execute('DELETE FROM user WHERE isAdmin = False')
    db.session.commit()
    users = [{
        'username': 'user1',
        'email': 'user1@ua.pt',
        'password': 'password1',
        'first_name': 'user',
        'last_name': 'one',
        'isAdmin': False,
        'phone_number': '123456789',
        'image': 'default.png',
        'address': 'Aveiro'
    }, {
        'username': 'user2',
        'email': 'user2@ua.pt',
        'password': 'password2',
        'first_name': 'user',
    },{
        'username': 'lucifer666',
        'email': 'lucifer666@ua.pt',
        'password': 'hell',
        'first_name': 'Lucifer',
        'isAdmin': True
    }]
    try:
        db.session.bulk_insert_mappings(User, users)
        db.session.commit()
        return jsonify({'message': 'Users created successfully!'})
    except Exception as e:
        print(e)
        return jsonify({'message': 'Error creating users!'})

@database.route('/generate/products', methods=['GET'])
def create_products():
    db.session.execute('DELETE FROM product')
    db.session.commit()
    products= [{
        'name': 'Coca-Cola',
        'price': 1.5,
        'category_id': 1,},
        {
        'name': 'Pepsi',
        'price': 1.5,
        'category_id': 1,
        },
        {
        'name': 'Fanta',
        'price': 1.5,
        'category_id': 1,
        }]
    try:    
        db.session.bulk_insert_mappings(Product, products)
        db.session.commit()
        return jsonify({'message': 'Products created successfully!'})  
    except Exception as e:
        print(e)
        return jsonify({'message': 'Error creating products!'})
    
@database.route('/generate/categories', methods=['GET'])
def create_categories():
    db.session.execute('DELETE FROM category')
    db.session.commit()
    categories = [{
        'name': 'Bebidas',
    }, {
        'name': 'Comida',
    }]
    try:
        db.session.bulk_insert_mappings(Category, categories)
        db.session.commit()
        return jsonify({'message': 'Categories created successfully!'})
    except Exception as e:
        print(e)
        return jsonify({'message': 'Error creating categories!'})
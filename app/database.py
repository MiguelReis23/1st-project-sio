from app import db
from app.models import User


def create_dummy_data():
    # Delete all existing users
    User.query.delete()

    # Generate new users
    user1 = User(username='user1', email='user1@example.com', password='password1')
    user2 = User(username='user2', email='user2@example.com', password='password2')
    user3 = User(username='user3', email='user3@example.com', password='password3')

    # Add users to the database
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.commit()
from database import Database

class Database:
    def __init__(self):
        self.customers = []

    def add_customer(self, name, email, user_id):
        customer_id = user_id  # set the customer id to be equal to the user id
        customer = {"id": customer_id, "name": name, "email": email}
        self.customers.append(customer)

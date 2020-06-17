from my_app import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    debts = db.relationship('Debt')

    def __init__(self, name, email):
        self.name = name
        self.email = email

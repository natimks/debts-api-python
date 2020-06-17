from my_app import db


class Debt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(150))
    value = db.Column(db.Float)
    paid = db.Column(db.Boolean)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))

    def __init__(self, description, value, paid, person_id):
        self.description = description
        self.value = value
        self.paid = paid
        self.person_id = person_id


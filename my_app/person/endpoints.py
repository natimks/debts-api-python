from flask import request, jsonify, Blueprint
from my_app import db
from my_app.person.model import Person

person_route = Blueprint('person_route', __name__)


@person_route.route('/')
def index():
    people = Person.query.all()

    result = []

    for person in people:
        data = {}

        data['id'] = person.id
        data['name'] = person.name
        data['email'] = person.email

        result.append(data)

    return jsonify(result)


@person_route.route('/person', methods=['POST'])
def insert():
    name = request.json['name']
    email = request.json['email']

    person = Person(name, email)
    db.session.add(person)
    db.session.commit()

    return f'Pessoa {name} inserida com sucesso!'


@person_route.route('/person/<id>', methods=['GET'])
def get(id):
    person = Person.query.get(id)
    result = {
        'id': person.id,
        'name': person.name,
        'email': person.email
    }

    return jsonify(result)


@person_route.route('/person', methods=['PUT'])
def update():
    id = request.json['id']

    person = Person.query.get(id)
    person.name = request.json['name']
    person.email = request.json['email']

    db.session.commit()

    return 'Pessoa atualizada com sucessso!'


@person_route.route('/person/<id>', methods=['DELETE'])
def delete(id):
    person = Person.query.get(id)
    db.session.delete(person)
    db.session.commit()
    return 'Pessoa removida com sucesso!'

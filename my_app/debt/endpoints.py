from flask import request, jsonify, Blueprint
from my_app import db
from my_app.debt.model import Debt
from my_app.debt.utils import format_debts
from my_app.person.model import Person

debt_route = Blueprint('debt_route', __name__)


@debt_route.route('/debt')
def get_all():
    debts = Debt.query.all()

    result = format_debts(debts)

    return jsonify(result)


@debt_route.route('/debt', methods=['POST'])
def insert():
    description = request.json['description']
    value = request.json['value']
    paid = request.json['paid']
    person_id = request.json['person_id']

    debt = Debt(description, value, paid, person_id)
    db.session.add(debt)
    db.session.commit()

    return f'Dívida {description} inserida com sucesso!'


@debt_route.route('/debt/<id>', methods=['GET'])
def get(id):
    debt = Debt.query.get(id)
    result = {
        'id': debt.id,
        'description': debt.description,
        'value': debt.value,
        'paid': debt.paid,
        'person_id': debt.person_id
    }

    return jsonify(result)


@debt_route.route('/debt', methods=['PUT'])
def update():
    id = request.json['id']

    debt = Debt.query.get(id)
    debt.description = request.json['description']
    debt.value = request.json['value']
    debt.paid = request.json['paid']
    debt.person_id = request.json['person_id']

    db.session.commit()

    return f'Dívida {debt.description} atualizada com sucessso!'


@debt_route.route('/debt/<id>', methods=['DELETE'])
def delete(id):
    debt = Debt.query.get(id)
    db.session.delete(debt)
    db.session.commit()
    return 'Dívida removida com sucesso!'


@debt_route.route('/person/debts/<person_id>', methods=['GET'])
def get_debts_by_person_id(person_id):
    person = Person.query.get(person_id)

    debts = format_debts(person.debts)

    result = {
        'id': person.id,
        'name': person.name,
        'email': person.email,
        'debts': debts
    }

    return jsonify(result)


@debt_route.route('/debt/payment', methods=['PUT'])
def pay_debt():
    id = request.json['id']

    debt = Debt.query.get(id)

    if debt.paid:
        return f'Dívida {debt.description} já se encontra paga!'

    debt.paid = True
    db.session.commit()

    return f'Dívida {debt.description} paga com sucessso!'


@debt_route.route('/debt/paid', methods=['GET'])
def get_all_paid_debts():
    debts = Debt.query.filter(Debt.paid).all()

    result = format_debts(debts)

    return jsonify(result)

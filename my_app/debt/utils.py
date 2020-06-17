def format_debts(debts):
    result = []

    for debt in debts:
        data = {}

        data['id'] = debt.id
        data['description'] = debt.description
        data['value'] = debt.value
        data['paid'] = debt.paid
        data['person_id'] = debt.person_id

        result.append(data)

    return result

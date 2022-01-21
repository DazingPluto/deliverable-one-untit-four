from glob import escape
from flask import Flask, request, jsonify
import json

app = Flask(__name__)


f = open('data.json')


payload = json.load(f)
data = payload.get('data')

old_email = data[0]['email'].split('@')

new_email = data[0]['credit_card'].split('\n')[1].replace(
    ' ', '').lower() + '@' + old_email[1]


jeremy = {
    'ssn': data[0]['ssn'],
    'phone_number': data[0]['phone_number'],
    'email': new_email,
    'credit_card': {
        'type': data[0]['credit_card'].split('\n')[0].split(' ')[0],
        'name': data[0]['credit_card'].split('\n')[1],
        'number': int(data[0]['credit_card'].split('\n')[2].split(' ')[0]),
        'expiration': data[0]['credit_card'].split('\n')[2].split(' ')[1],
    }
}
jeremy['credit_card'][data[0]['credit_card'].split('\n')[3].split(' ')[
    0].split(':')[0]] = data[0]['credit_card'].split('\n')[3].split(' ')[1]

cc = data[0]['credit_card'].split('\n')

cc_type = cc[0].split(' ')[0]

name = cc[1]

cc_number = int(cc[2].split(' ')[0])  

cvc = cc[3].split(' ')[1]

new_data = []
for i in range(len(data)):
    person = data[i]  

    credit_card_data = person['credit_card'].split('\n')
    credit_card_type = credit_card_data[0]
    name = credit_card_data[1]

    number = credit_card_data[2].split(' ')[0]
    expiration = credit_card_data[2].split(' ')[1]
    credit_card_code = credit_card_data[3]
    credit_card_code = credit_card_code.split(': ')
    credit_card_key = credit_card_code[0]
    code = credit_card_code[1]

    if 'VISA' in credit_card_type:
        credit_card_type = credit_card_type.split(' ')[0]

    elif 'Discover' in credit_card_type:
        pass
    elif 'American Express' in credit_card_type:
        pass
    elif 'Diners Club' in credit_card_type:
        credit_card_type = 'Diners Club'
    elif 'JCB' in credit_card_type:
        credit_card_type = credit_card_type.split(' ')[0]
    elif 'Maestro' in credit_card_type:
        pass
    elif 'Mastercard' in credit_card_type:
        pass

    old_email = person['email'].split('@')
    domain_name = old_email[1]
    email = name.replace(' ', '').lower() + '@' + domain_name

    address = person['address'].split('\n')
    street = address[0]
    if ',' in address[1]:
        city = address[1].split(', ')[0]
        state = address[1].split(', ')[1].split(' ')[0]
        zipcode = address[1].split(', ')[1].split(' ')[1]
    else:
        city = address[1].split(' ')[0]
        state = address[1].split(' ')[1]
        zipcode = address[1].split(' ')[2]

    obj = {
        'ssn': person['ssn'],
        'phone_number': person['phone_number'],
        'email': email,
        'credit_card': {
            'type': credit_card_type,
            'number': number,
            'expiration': expiration,
        },
        'job': person['job'],
        'favorite_color': person['favorite_color'],
        'name': name,
        'address': {
            'street': street,
            'city': city,
            'state': state,
            'zipcode': zipcode
        }
    }
    obj['credit_card'][credit_card_key] = code

    new_data.append(obj)

favorite_color_blue = list(
    filter(lambda person: person.get('favorite_color') == 'navy', new_data))

favorite_color_red = list(
    filter(lambda person: person.get('favorite_color') == 'red', new_data))

favorite_color_pink = list(
    filter(lambda person: person.get('favorite_color') == 'pink', new_data))

favorite_color_maroon = list(
    filter(lambda person: person.get('favorite_color') == 'maroon', new_data))

american_express_users = list(
    filter(lambda person: person['credit_card']['type'] == 'American Express',
           new_data))

american_express_users_ca = list(
    filter(lambda person: person['address']['state'] == 'CA',
           american_express_users))

cto = list(
    filter(lambda person: person['job'] == 'Chief Technology Officer',
           new_data))

gmail_users = list(filter(lambda person: 'gmail' in person['email'], new_data))


@app.route("/")
def hello_world():
    obj = {"message": "Hello World", "year": "2022"}
    data = json.dumps(obj)
    return data


@app.route('/blue')
def fetch_blue():
    obj = {'blue': favorite_color_blue, 'amount': len(favorite_color_blue)}
    data = json.dumps(obj)
    return data


@app.route('/states/<state>')
def show_state(state):
    state = state.upper()
    us_states_list = list(
        filter(lambda person: person['address']['state'] == f'{state}', 
               new_data))
    new_list = []
    for person in us_states_list:
        person.pop('ssn', None)
        new_list.append(person)

    obj = {'people': new_list, 'amount': len(new_list)}
    data = json.dumps(obj)
    return data


@app.route('/address')
def get_address():
    new_list = []
    for person in range(len(data)):
        address = data[person]['address']
        new_list.append(address)
    obj = {
        'address': new_list,
        'amount': len(new_list)
    }
    datas = json.dumps(obj)
    return datas

@app.route('/email')
def get_address():
    new_list = []
    for person in range(len(data)):
        address = data[person]['email']
        new_list.append(address)
    obj = {
        'address': new_list,
        'amount': len(new_list)
    }
    datas = json.dumps(obj)
    return datas


@app.route('/states', methods=['POST'])
def show_states():
    error = None
    if request.method == 'POST':
        print('state ->', request.form['state'])
        state = request.form['state']
        state = state.upper()
        us_states_list = list(
            filter(lambda person: person['address']['state'] == f'{state}',
                   new_data))
        new_list = []
        for person in us_states_list:
            person.pop('ssn', None)
            new_list.append(person)

        obj = {'people': new_list, 'amount': len(new_list)}
        data = json.dumps(obj)
        return data
    else:
        error = 'Not data return. Please try again.'
        return error

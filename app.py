from flask import Flask, jsonify, request, render_template

# inicia o flask
app = Flask(__name__)

stores = [
    {
        'name': 'Loja 1',
        'items': [
            {
                'name': 'meu item',
                'price': 15.99
            }
        ]
    }

]


@app.route('/')  # ex: 'http://www.google.com/' - home
# define o que vai ser apresentado quando entrar na home
def home():
    return render_template('index.html')

# post /store data:{name:}
@app.route('/store', methods=['POST'])  # acessível apenas por post request
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# get /store/<string:name>
@app.route('/store/<string:name>')  # identifica como GET automaticamente
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


# get /store
@app.route('/store')  # identifica como GET automaticamente
def get_stores():
    return jsonify({'stores': stores})

# post /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

# get /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})


app.run(port=5000)  # especifica a porta que vai rodar

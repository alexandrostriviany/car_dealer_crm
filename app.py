import json

from flask import Flask, jsonify, request

import Crm

app = Flask(__name__)


@app.route('/')
def ping():
    return "{I'm working!}"


@app.route('/dealers/add', methods=['POST'])
def add_dealer():
    try:
        record = json.loads(request.data)
    except ValueError:
        return jsonify({"error": "Bad request"}), 400
    if 'name' not in record.keys():
        return jsonify({"error": "Please add 'name' value for Dealer Center"}), 400
    return jsonify({'message': Crm.add_dealer_center(record['name'])}), 201


@app.route('/dealers/<dc_id>', methods=['DELETE'])
def delete_dealer(dc_id):
    r = Crm.delete_dealer_center_by_id(dc_id)
    return jsonify({'message' if r[1] == 200 else 'error': r[0]}), r[1]


@app.route('/dealers/list', methods=['GET'])
def dealer_list():
    return jsonify({'Dealer Centers': Crm.dealer_center_list_filtered(**request.args) if len(
        request.args) > 0 else Crm.dealer_centers_list()})


@app.route('/car/add', methods=['POST'])
def add_car():
    try:
        record = json.loads(request.data)
    except ValueError:
        return jsonify({"error": "Bad request"}), 400
    if ('name' or 'color' or 'dc_id') not in record.keys():
        return jsonify({"error": "Please check if it's all parameters were added"}), 400
    r = Crm.add_car(record['name'], record['color'], record['dc_id'])
    return jsonify({'message' if r[1] == 201 else 'error': r[0]}), r[1]


@app.route('/car/<car_id>', methods=['DELETE'])
def delete_car(car_id):
    r = Crm.delete_car_by_id(car_id)
    return jsonify({'message' if r[1] == 200 else 'error': r[0]}), r[1]


@app.route('/car/list', methods=['GET'])
def car_list():
    if len(request.args) > 0:
        return jsonify({'Cars': Crm.car_list_filtered(**request.args)})
    else:
        return jsonify({'Cars': Crm.car_list()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')

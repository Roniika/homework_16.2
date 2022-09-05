import json
from flask import request, jsonify
from config import app
from service import *


@app.route("/users", methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        return jsonify(get_all_users())
    elif request.method == 'POST':
        new_item = insert_data(request.json, User)

        return jsonify(new_item.to_dict())


@app.route("/users/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def get_user_by_id(user_id):
    if request.method == 'GET':
        data = get_all_users_by_id(user_id)
        return jsonify(data)
    elif request.method == 'PUT':
        item = update_universal(User, user_id, request.json)
        return jsonify(item.to_dict())
    elif request.method == 'DELETE':
        delete_universal(User, user_id)
        return '', 204


@app.route("/orders", methods=['GET', 'POST'])
def get_orders():
    if request.method == 'GET':
        return jsonify(get_all_orders())
    elif request.method == 'POST':
        new_item = insert_data(request.json, Order)

        return jsonify(new_item.to_dict())


@app.route("/orders/<int:order_id>", methods=['GET', 'PUT', 'DELETE'])
def get_order_by_id(order_id):
    if request.method == 'GET':
        data = get_all_orders_by_id(order_id)
        return jsonify(data)
    elif request.method == 'PUT':
        item = update_universal(Order, order_id, request.json)
        return jsonify(item.to_dict())
    elif request.method == 'DELETE':
        delete_universal(Order, order_id)
        return '', 204


@app.route("/offers", methods=['GET', 'POST'])
def get_offers():
    if request.method == 'GET':
        return jsonify(get_all_offers())
    elif request.method == 'POST':
        new_item = insert_data(request.json, Offer)

        return jsonify(new_item.to_dict())


@app.route("/offers/<int:offer_id>", methods=['GET', 'PUT', 'DELETE'])
def get_offer_by_id(offer_id):
    if request.method == 'GET':
        data = get_all_offers_by_id(offer_id)
        return jsonify(data)
    elif request.method == 'PUT':
        item = update_universal(Offer, offer_id, request.json)
        return jsonify(item.to_dict())
    elif request.method == 'DELETE':
        delete_universal(Offer, offer_id)
        return '', 204


if __name__ == '__main__':
    init_db()
    app.run(
        host='0.0.0.0',
        port=8088,
        debug=True
    )

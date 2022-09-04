import json
from flask import request
from config import app
from service import *


@app.route("/users", methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all_users(), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_user()
        elif isinstance(request.json, dict):
            insert_data_user([request.json])
        else:
            print("Непонятный тип данных")

        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/users/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def get_user_by_id(user_id):
    if request.method == 'GET':
        data = get_all_users_by_id(user_id)

        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
            )
    elif request.method == 'PUT':
        update_universal(User, user_id, request.json)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        delete_universal(User, user_id)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/orders", methods=['GET', 'POST'])
def get_orders():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all_orders(), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_order()
        elif isinstance(request.json, dict):
            insert_data_order([request.json])
        else:
            print("Непонятный тип данных")

        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/orders/<int:order_id>", methods=['GET', 'PUT', 'DELETE'])
def get_order_by_id(order_id):
    if request.method == 'GET':
        data = get_all_orders_by_id(order_id)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        update_universal(Order, order_id, request.json)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        delete_universal(Order, order_id)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/offers", methods=['GET', 'POST'])
def get_offers():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all_offers(), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_offer()
        elif isinstance(request.json, dict):
            insert_data_offer([request.json])
        else:
            print("Непонятный тип данных")

        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/offers/<int:offer_id>", methods=['GET', 'PUT', 'DELETE'])
def get_offer_by_id(offer_id):
    if request.method == 'GET':
        data = get_all_offers_by_id(offer_id)

        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
            )
    elif request.method == 'PUT':
        update_universal(Offer, offer_id, request.json)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        delete_universal(Offer, offer_id)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


if __name__ == '__main__':
    init_db()
    app.run(
        host='0.0.0.0',
        port=8088,
        debug=True
    )

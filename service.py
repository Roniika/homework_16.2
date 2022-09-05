from models import *
from config import db
import json


def insert_data(data, model):
    new_item = model(**data)
    db.session.add(new_item)
    db.session.commit()
    return new_item


def get_all_users():
    result = []
    for row in User.query.all():
        result.append(row.to_dict())

    return result


def get_all_users_by_id(user_id):
    try:
        return db.session.query(User).get(user_id).to_dict()
    except Exception:
        return {}


def get_all_orders():
    result = []
    for row in Order.query.all():
        result.append(row.to_dict())

    return result


def get_all_orders_by_id(order_id):
    try:
        return db.session.query(Order).get(order_id).to_dict()
    except Exception:
        return {}


def get_all_offers():
    result = []
    for row in Offer.query.all():
        result.append(row.to_dict())

    return result


def get_all_offers_by_id(offer_id):
    try:
        return db.session.query(Offer).get(offer_id).to_dict()
    except Exception:
        return {}


def update_universal(model, pk, values):
    item = db.session.query(model).get(pk)
    if not item:
        raise IndexError("Элемент с таким id не найден")
    for attribute, new_value in values.items():
        setattr(item, attribute, new_value)

    return item


def delete_universal(model, user_id):
    try:
        db.session.query(model).filter(model.id == user_id).delete()
        db.session.commit()

    except Exception:
        return {}


def init_db():
    db.drop_all()
    db.create_all()

    with open("data/user.json") as file:
        data = json.load(file)
    users_to_append = [User(**kwarg) for kwarg in data]
    db.session.add_all(users_to_append)

    with open("data/order.json") as file:
        data = json.load(file)
    orders_to_append = [Order(**kwarg) for kwarg in data]
    db.session.add_all(orders_to_append)

    with open("data/offer.json") as file:
        data = json.load(file)
    offers_to_append = [Offer(**kwarg) for kwarg in data]
    db.session.add_all(offers_to_append)

    db.session.commit()



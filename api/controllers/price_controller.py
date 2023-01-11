from flask import jsonify


def calculate_price(body):
    print(body)
    return jsonify({'id':body['id'], 'price_category':'High'})

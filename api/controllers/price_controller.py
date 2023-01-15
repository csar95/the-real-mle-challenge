from flask import jsonify
import pandas as pd
from catboost import CatBoostClassifier


model = CatBoostClassifier()
model.load_model("./catboost-model-depth12-iter200-l2reg1_5-lr0_1")


def calculate_price(body):
    print(body)

    if body['room_type'] in ['Private room','Shared room']:
        body['room_type'] = 'Private-Share room'

    if body['neighbourhood'] in ['Bronx','Queens','Staten Island']:
        body['neighbourhood'] = 'Bronx-Queens-StatenIsland'

    # DataFrame con una sola fila que contiene las variables extraídas a partir del body recibido y con las columnas en el orden que espera el modelo
    X = pd.DataFrame(body, index=[0])[model.feature_names_]
    price_class = model.predict(X)[0][0]

    price_classes = {0:'Low',1:'Mid',2:'High',3:'Luxury'}

    return jsonify({'id':body['id'], 'price_category':price_classes[price_class]})

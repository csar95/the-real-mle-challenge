from flask import Flask, request
from flasgger import Swagger, LazyJSONEncoder, swag_from
from controllers.price_controller import calculate_price


app = Flask(__name__)
app.json_encoder = LazyJSONEncoder

swagger_template = dict(
    info = {
        'title': "The MLE Challenge",
        'version': "0.0.1",
        'description': "This API allows the server to receive listing data from Airbnb to predict the price category."
    }
)

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'data_input',
            "route": '/data_input.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,  # Allow access to Swagger UI
    "specs_route": "/apidocs/"
}

swagger = Swagger(app, template=swagger_template, config=swagger_config)

@app.route("/data_input", methods=['POST'])
@swag_from("swagger/data_input.yml", validation=True)
def data_input_handler():
    return calculate_price(body=request.json)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

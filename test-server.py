# create flask server to test the model

import json
from typing import Callable
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from werkzeug.exceptions import BadRequest, HTTPException

UI_URL = "http://localhost:5173"  # TODO: add UI URL
MODEL_PATH = "MODEL_PATH"  # TODO: add model path


app = Flask(__name__)
cors_options = {"origins": UI_URL}
cors = CORS(app, resources={r"/predict": cors_options, r"/": cors_options})


def mk_predict(model_path) -> Callable:
    # TODO: load model and return predict function
    return lambda x: x


predict = mk_predict(MODEL_PATH)


def is_valid_request(data):
    # TODO: add validation
    return data["text"] not in ["test error", ""]


def make_error(data):
    # TODO: add error handling
    return jsonify({"error": f"Bad request: {data}"}), 400


def preprocess_request(data):
    return data


def format_prediction(prediction) -> dict:
    # TODO: format prediction
    return prediction


@app.route("/predict", methods=["POST"])
def _():
    data = request.get_json()
    if not is_valid_request(data):
        return make_error(data)
    data = preprocess_request(data)
    prediction = predict(data)
    return jsonify(format_prediction(prediction))


if __name__ == "__main__":
    app.run(debug=True)

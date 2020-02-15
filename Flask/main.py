from flask import Flask, request
from flask_restful import Api, Resource
from SMART_trash import *
import sys
import numpy as np

app = Flask(__name__)
api = Api(app)


class User(Resource):
    def get(self):
        return "Hello world", 200

    def post(self):
        # image = request.json['files']
        # result = new_AI.evaluate(np.array(image))
        image = request.files['files']
        result = new_AI.evaluate(image)
        print(image, file=sys.stderr)

        try:
            # print('enter')
            # recyclability = evaluate(image)
            return {"return": result}, 200

        except:
            return "Error", 400


if __name__ == '__main__':
    new_AI = AI()
    new_AI.loadmodel('../models/InceptionV3.h5')
    new_AI.loadLabel('./24hackton_label.txt')
    api.add_resource(User, "/")
    app.run(debug=True)

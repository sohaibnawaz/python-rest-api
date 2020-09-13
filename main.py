from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {
    "jeff": {"age": 45, "gender": "male"},
    "alex": {"age": 26, "gender": "male"},
    "lucy": {"age": 27, "gender": "female"}
}

class HelloWorld(Resource):
    def get(self, name):
        return names[name]

api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)

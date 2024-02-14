from flask_restx import Resource, Namespace

# base api route
test = Namespace("test")


@test.route("/")
class Test(Resource):
    def get(self):
        return {"hello world": "this is a test"}

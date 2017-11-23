from flask import Blueprint, request

from app.app import mongo
from app.helpers.handler import Handler

user_endpoint = Blueprint("user", __name__)


# POST
# user_details: { forename: <>, surname: <>, number: <> }
@user_endpoint.route("/create", methods=["POST"])
def create_user():
    data = request.json

    if User.does_user_exist(data["number"]):
        return Handler.get_json_res({"success": False, "reason": "user_already_exists"})

    data["verified"] = True
    data["creation_time"] = Handler.get_current_time_in_millis()
    mongo.db.users.save(data)

    return Handler.get_json_res({"success": True})


# POST { number: <> }
@user_endpoint.route("/get-others", methods=["POST"])
def get_other_users():
    number = request.json["number"]
    other_users = mongo.db.users.find({"number": {"$nin": [number]}})
    return Handler.get_json_res(other_users)


class User:
    @staticmethod
    def get_user(number):
        if User.does_user_exist(number):
            return list(mongo.db.users.find({"number": number}))[0]
        return {}

    @staticmethod
    def does_user_exist(number):
        return mongo.db.users.find({"number": number}).count() > 0

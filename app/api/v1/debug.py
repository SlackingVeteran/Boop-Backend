from flask import Blueprint

from app.app import mongo
from app.helpers.handler import Handler

debug_endpoint = Blueprint("debug", __name__)


@debug_endpoint.route("/get-all-users", methods=["GET", "POST"])
def get_all_users():
    return Handler.get_json_res(list(mongo.db.users.find()))

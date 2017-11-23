from flask import Blueprint

from app.helpers.handler import Handler

services_endpoint = Blueprint("services", __name__)


@services_endpoint.route("/verify-number", methods=["GET", "POST"])
def verify_number():
    return Handler.get_json_res({"success": True})

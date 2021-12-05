from flask import render_template
from flask import Blueprint


registrations_blueprint = Blueprint("registration", __name__)


@registrations_blueprint.route("/registration")
def register():
    return render_template("/registration.html")

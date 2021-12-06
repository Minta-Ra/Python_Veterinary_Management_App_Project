from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.appointment import Appointment
import repositories.appointment_repository as appointment_repository


appointments_blueprint = Blueprint("appointments", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/appointments'
@appointments_blueprint.route("/appointments")
def appointments():
    appointments = appointment_repository.select_all()
    return render_template("appointments/index.html", appointments=appointments)

# NEW
# GET '/appointments/new'

# CREATE
# POST '/appointments'

# SHOW
# GET '/appointments/<id>'

# EDIT
# GET '/appointments/<id>/edit'

# UPDATE
# PUT '/appointments/<id>'

# DELETE
# DELETE '/appointments/<id>'
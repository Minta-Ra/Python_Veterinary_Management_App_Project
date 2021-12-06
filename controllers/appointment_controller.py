from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.appointment import Appointment
import repositories.appointment_repository as appointment_repository
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository


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
@appointments_blueprint.route("/appointments/new", methods=["GET"])
def new_appointment():
    pets = pet_repository.select_all()
    vets = vet_repository.select_all()
    return render_template("appointments/new.html", pets=pets, vets=vets)

# CREATE
# POST '/appointments'
@appointments_blueprint.route("/appointments", methods=["POST"])
def add_new_appointment():
    pet_id = request.form["pet_id"]
    appointment_date = request.form["appointment_date"]
    check_in = request.form["check_in"]
    check_out = request.form["check_out"]
    vet_id = request.form["vet_id"]
    pet = pet_repository.select(pet_id)
    vet = vet_repository.select(vet_id)
    appointment = Appointment(pet, appointment_date, check_in, check_out, vet)
    appointment_repository.save(appointment)
    return redirect("/appointments")

# SHOW
# GET '/appointments/<id>'
@appointments_blueprint.route("/appointments/<id>")
def show_appointments(id):
    appointment = appointment_repository.select(id)
    return render_template("appointments/show.html", appointment=appointment)

# EDIT
# GET '/appointments/<id>/edit'
@appointments_blueprint.route("/appointments/<id>/edit")
def edit_appointment(id):
    appointment = appointment_repository.select(id)
    pets = pet_repository.select_all()
    vets = vet_repository.select_all()
    return render_template("appointments/edit.html", appointment=appointment, pets=pets, vets=vets)

# UPDATE
# PUT '/appointments/<id>'
@appointments_blueprint.route("/appointments/<id>", methods=["POST"])
def update_appointment_details(id):
    pet_id = request.form["pet_id"]
    appointment_date = request.form["appointment_date"]
    check_in = request.form["check_in"]
    check_out = request.form["check_out"]
    vet_id = request.form["vet_id"]
    pet = pet_repository.select(pet_id)
    vet = vet_repository.select(vet_id)
    appointment = Appointment(pet, appointment_date, check_in, check_out, vet, id)
    appointment_repository.update(appointment)
    return redirect("/appointments")

# DELETE
# DELETE '/appointments/<id>'
@appointments_blueprint.route("/appointments/<id>/delete", methods=["POST"])
def delete_appointment(id):
    appointment_repository.delete(id)
    return redirect("/appointments")
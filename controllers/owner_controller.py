import re
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.owner import Owner
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository


owners_blueprint = Blueprint("owners", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/owners'
@owners_blueprint.route("/owners")
def owners():
    owners = owner_repository.select_all()
    return render_template("owners/index.html", owners=owners)

# NEW
# GET '/owners/new'
@owners_blueprint.route("/owners/new")
def new_owner():
    return render_template("owners/new.html")

# CREATE
# POST '/owners'
@owners_blueprint.route("/owners", methods=["POST"])
def add_new_owner():
    name = request.form["name"]
    phone_number = request.form["phone_number"]
    registration = request.form["registration"]
    owner = Owner(name, phone_number, registration)
    owner_repository.save(owner)
    return redirect("/owners")

# SHOW
# GET '/owners/<id>'
@owners_blueprint.route("/owners/<id>")
def show(id):
    owner = owner_repository.select(id)
    return render_template("owners/show.html", owner=owner)

# EDIT
# GET '/owners/<id>/edit'

# UPDATE
# PUT '/owners/<id>'

# DELETE
# DELETE '/owners/<id>'
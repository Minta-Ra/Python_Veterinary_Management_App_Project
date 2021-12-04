import re
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.vet import Vet
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository
import repositories.pet_repository as pet_repository


vets_blueprint = Blueprint("veterinarians", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/vets'
@vets_blueprint.route("/veterinarians")
def vets():
    vets = vet_repository.select_all()
    return render_template("vets/index.html", vets=vets)

#################################################################
#########  owners=owners, pets=pets - maybe not needed???
# NEW
# GET '/vets/new'
# @vets_blueprint.route("/veterinarians/new", methods=["GET"])
# def new_vet():
#     owners = owner_repository.select_all()
#     pets = pet_repository.select_all()
#     return render_template("vets/new.html", owners=owners, pets=pets)


@vets_blueprint.route("/veterinarians/new", methods=["GET"])
def new_vet():
    return render_template("vets/new.html")


# CREATE
# POST '/vets'
@vets_blueprint.route("/veterinarians", methods=["POST"])
def add_new_vet():
    name = request.form["name"]
    experience = request.form["experience"]
    vet = Vet(name, experience)
    vet_repository.save(vet)
    return redirect("/veterinarians")

# SHOW
# GET '/vets/<id>'
@vets_blueprint.route("/veterinarians/<id>")
def show(id):
    vet = vet_repository.select(id)
    return render_template("vets/show.html", vet=vet)

# EDIT
# GET '/vets/<id>/edit'
@vets_blueprint.route("/veterinarians/<id>/edit")
def edit_vet(id):
    vet = vet_repository.select(id)
    return render_template("vets/edit.html", vet=vet)

# UPDATE
# PUT '/vets/<id>'
@vets_blueprint.route("/veterinarians/<id>", methods=["POST"])
def update_vet_details(id):
    name = request.form["name"]
    experience = request.form["experience"]
    vet = Vet(name, experience, id)
    vet_repository.update(vet)
    return redirect("/veterinarians")


# DELETE
# DELETE '/vets/<id>'
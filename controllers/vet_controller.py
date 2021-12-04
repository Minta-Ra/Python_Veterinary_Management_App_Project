from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.vet import Vet
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository


vets_blueprint = Blueprint("veterinarians", __name__)

@vets_blueprint.route("/veterinarians")
def vets():
    vets = vet_repository.select_all()
    return render_template("vets/index.html", vets=vets)

# @vets_blueprint.route("/veterinarians/<id>")
# def show(id):
#     vet = vet_repository.select(id)
#     owners = owner_repository.owners(vet)
#     return render_template("vets/show.html", vet=vet, owners=owners)


# RESTful CRUD Routes

# INDEX
# GET '/tasks'

# NEW
# GET '/tasks/new'

# CREATE
# POST '/tasks'

# SHOW
# GET '/tasks/<id>'

# EDIT
# GET '/tasks/<id>/edit'

# UPDATE
# PUT '/tasks/<id>'

# DELETE
# DELETE '/tasks/<id>'
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.pet import Pet
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository
import repositories.pet_repository as pet_repository


pets_blueprint = Blueprint("pets", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/pets'
@pets_blueprint.route("/pets")
def pets():
    pets = pet_repository.select_all()
    return render_template("pets/index.html", pets=pets)


# NEW
# GET '/pets/new'

# CREATE
# POST '/pets'

# SHOW
# GET '/pets/<id>'

# EDIT
# GET '/pets/<id>/edit'

# UPDATE
# PUT '/pets/<id>'

# DELETE
# DELETE '/pets/<id>'
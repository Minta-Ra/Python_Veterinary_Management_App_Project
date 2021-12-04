from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.owner import Owner
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository


owners_blueprint = Blueprint("owners", __name__)

@owners_blueprint.route("/owners")
def owners():
    owners = owner_repository.select_all()
    return render_template("owners/index.html", owners=owners)

# RESTful CRUD Routes

# INDEX
# GET '/owners'

# NEW
# GET '/owners/new'

# CREATE
# POST '/owners'

# SHOW
# GET '/owners/<id>'

# EDIT
# GET '/owners/<id>/edit'

# UPDATE
# PUT '/owners/<id>'

# DELETE
# DELETE '/owners/<id>'
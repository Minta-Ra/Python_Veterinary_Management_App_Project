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
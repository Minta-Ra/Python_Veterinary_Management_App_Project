from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.owner import Owner
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository


owners_blueprint = Blueprint("owners", __name__)

# RESTful CRUD Routes
# INDEX # GET '/owners'
@owners_blueprint.route("/owners")
def owners():
    owners = owner_repository.select_all()
    # Bring all pets of specific owner
    for owner in owners:
        owner_pets = owner_repository.bring_owner_pets(owner.id)
        owner.my_pets = owner_pets
    return render_template("owners/index.html", owners=owners)

# NEW # GET '/owners/new'
@owners_blueprint.route("/owners/new")
def new_owner():
    return render_template("owners/new.html")

# CREATE # POST '/owners'
@owners_blueprint.route("/owners", methods=["POST"])
def add_new_owner():
    name = request.form["name"]
    phone_number = request.form["phone_number"]

    if "registration" in request.form.keys():
        registration = True
    else:
        registration = False

    owner = Owner(name, phone_number, registration)
    owner_repository.save(owner)

    if "register" in request.form.keys():
        return redirect("/pets/new")
    else:
        return redirect("/owners")

# SHOW # GET '/owners/<id>'
@owners_blueprint.route("/owners/<id>")
def show(id):
    owner = owner_repository.select(id)
    return render_template("owners/show.html", owner=owner)

# EDIT # GET '/owners/<id>/edit'
@owners_blueprint.route("/owners/<id>/edit")
def edit_owner(id):
    owner = owner_repository.select(id)
    return render_template("owners/edit.html", owner=owner)

# UPDATE # PUT '/owners/<id>'
@owners_blueprint.route("/owners/<id>", methods=["POST"])
def update_owner_details(id):
    name = request.form["name"]
    phone_number = request.form["phone_number"]

    if "registration" in request.form.keys():
        registration = True
    else:
        registration = False
        
    owner = Owner(name, phone_number, registration, id)
    owner_repository.update(owner)
    return redirect("/owners")

# DELETE # DELETE '/owners/<id>'
@owners_blueprint.route("/owners/<id>/delete", methods=["POST"])
def delete_owner(id):
    owner_repository.delete(id)
    return redirect("/owners")
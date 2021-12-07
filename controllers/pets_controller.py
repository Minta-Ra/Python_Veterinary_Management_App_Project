from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.pet import Pet
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository
import repositories.pet_repository as pet_repository


pets_blueprint = Blueprint("pets", __name__)

# RESTful CRUD Routes
# INDEX # GET '/pets'
@pets_blueprint.route("/pets")
def pets():
    pets = pet_repository.select_all()
    return render_template("pets/index.html", pets=pets)

# NEW # GET '/pets/new'
@pets_blueprint.route("/pets/new", methods=["GET"])
def new_pet():
    owners = owner_repository.select_all()
    vets = vet_repository.select_all()
    return render_template("pets/new.html", owners=owners, vets=vets)

# CREATE - ADD # POST '/pets'
@pets_blueprint.route("/pets", methods=["POST"])
def add_new_pet():
    name = request.form["name"]
    dob = request.form["dob"]
    pet_type = request.form["pet_type"]
    owner_id = request.form["owner_id"]
    vet_id = request.form["vet_id"]
    treatment_notes = request.form["treatment_notes"]
    owner = owner_repository.select(owner_id)
    vet = vet_repository.select(vet_id)
    pet = Pet(name, dob, pet_type, owner, vet, treatment_notes)
    pet_repository.save(pet)
    return redirect("/pets")

# SHOW # GET '/pets/<id>'
@pets_blueprint.route("/pets/<id>")
def show_pets(id):
    pet = pet_repository.select(id)
    return render_template("pets/show.html", pet=pet)

# EDIT # GET '/pets/<id>/edit'
@pets_blueprint.route("/pets/<id>/edit")
def edit_pet(id):
    pet = pet_repository.select(id)
    owners = owner_repository.select_all()
    vets = vet_repository.select_all()
    return render_template("pets/edit.html", pet=pet, owners=owners, vets=vets)

# UPDATE # PUT '/pets/<id>'
@pets_blueprint.route("/pets/<id>", methods=["POST"])
def update_pet_details(id):
    name = request.form["name"]
    dob = request.form["dob"]
    pet_type = request.form["pet_type"]
    owner_id = request.form["owner_id"]
    vet_id = request.form["vet_id"]
    treatment_notes = request.form["treatment_notes"]
    owner = owner_repository.select(owner_id)
    vet = vet_repository.select(vet_id)
    pet = Pet(name, dob, pet_type, owner, vet, treatment_notes, id)
    pet_repository.update(pet)
    return redirect("/pets")

# DELETE # DELETE '/pets/<id>'
@pets_blueprint.route("/pets/<id>/delete", methods=["POST"])
def delete_pet(id):
    pet_repository.delete(id)
    return redirect("/pets")
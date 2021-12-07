from db.run_sql import run_sql
from models.pet import Pet
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository


def save(pet):
    sql = "INSERT INTO pets (name, dob, pet_type, owner_id, vet_id, treatment_notes) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [pet.name, pet.dob, pet.pet_type, pet.owner.id, pet.vet.id, pet.treatment_notes]
    results = run_sql(sql, values)
    pet.id = results[0]['id']
    return pet

def select_all():
    pets = []
    sql = "SELECT * FROM pets"
    results = run_sql(sql)
    for row in results:
        owner = owner_repository.select(row['owner_id'])
        vet = vet_repository.select(row['vet_id'])
        pet = Pet(row['name'], row['dob'], row['pet_type'], owner, vet, row['treatment_notes'], row['id'])
        pets.append(pet)
    return pets

def select(id):
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    owner = owner_repository.select(result['owner_id'])
    vet = vet_repository.select(result['vet_id'])
    if result is not None:
        pet = Pet(result['name'], result['dob'], result['pet_type'], owner, vet, result['treatment_notes'], result['id'])
    return pet

def delete_all():
    sql = "DELETE  FROM pets"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM pets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(pet):
    sql = "UPDATE pets SET (name, dob, pet_type, owner_id, vet_id, treatment_notes) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [pet.name, pet.dob, pet.pet_type, pet.owner.id, pet.vet.id, pet.treatment_notes, pet.id]
    run_sql(sql, values)
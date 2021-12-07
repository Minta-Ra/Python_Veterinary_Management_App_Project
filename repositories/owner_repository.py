from db.run_sql import run_sql
from models.owner import Owner
from models.pet import Pet
import repositories.vet_repository as vet_repository


def save(owner):
    sql = "INSERT INTO owners (name, phone_number, registration) VALUES (%s, %s, %s) RETURNING id"
    values = [owner.name, owner.phone_number, owner.registration]
    results = run_sql(sql, values)
    owner.id = results[0]['id']
    return owner

def select_all():
    owners = []
    sql = "SELECT * FROM owners"
    results = run_sql(sql)
    for row in results:
        owner = Owner(row['name'], row['phone_number'], row['registration'], row['id'])
        owners.append(owner)
    return owners

def select(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        owner = Owner(result['name'], result['phone_number'], result['registration'], result['id'])
    return owner

def delete_all():
    sql = "DELETE  FROM owners"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM owners WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(owner):
    sql = "UPDATE owners SET (name, phone_number, registration) = (%s, %s, %s) WHERE id = %s"
    values = [owner.name, owner.phone_number, owner.registration, owner.id]
    run_sql(sql, values)

# Bring my pets
def bring_owner_pets(id):
    pets = []
    sql = "SELECT * FROM pets WHERE pets.owner_id = %s"
    values = [id]
    results = run_sql(sql, values)
    owner = select(id) # Calling select method and passing owners id
    for row in results:
        vet = vet_repository.select(row['vet_id'])
        pet = Pet(row['name'], row['dob'], row['pet_type'], owner, vet, row['treatment_notes'], row['id'])
        pets.append(pet)
    return pets

####################################
# Returns all owner's pets treated by specific vet
def owner_for_pet(owner):
    owner_for_pets = []
    sql = "SELECT owners.* FROM owners INNER JOIN pets ON pets.owner_id = owners.id WHERE vet_id = %s"
    values = [owner.id]
    results = run_sql(sql, values)
    for row in results:
        owner_for_pet = Owner(row['name'], row['phone_number'], row['registration'], row['id'])
        owner_for_pets.append(owner_for_pet)
    return owner_for_pets
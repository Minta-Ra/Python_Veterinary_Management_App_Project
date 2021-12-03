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

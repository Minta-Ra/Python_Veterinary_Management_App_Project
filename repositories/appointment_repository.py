from controllers.pet_controller import pets
from db.run_sql import run_sql
from models.appointment import Appointment
import repositories.vet_repository as vet_repository
import repositories.pet_repository as pet_repository


def save(appointment):
    sql = "INSERT INTO appointments (pet, appointment_date, check_in, check_out, vet) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [appointment.pet.id, appointment.appointment_date, appointment.check_in, appointment.check_out, appointment.vet.id]
    results = run_sql(sql, values)
    appointment.id = results[0]['id']
    return appointment

# Select all
def select_all():
    appointments = []
    sql = "SELECT * FROM appointments"
    results = run_sql(sql)
    for row in results:
        pet = pet_repository.select(row['pet_id'])
        vet = vet_repository.select(row['vet_id'])
        appointment = Appointment(pet, row['appointment_date'], row['check_in'], row['check_out'], vet, row['id'])
        appointments.append(appointment)
    return appointments

# Select
def select(id):
    appointment = None
    sql = "SELECT * FROM appointments WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    pet = pet_repository.select(result['pet_id'])
    vet = vet_repository.select(result['vet_id'])
    if result is not None:
        appointment = Appointment(pet, result['appointment_date'], result['check_in'], result['check_out'], vet, result['id'])
    return appointment

# Delete
def delete_all():
    sql = "DELETE  FROM appointments"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM appointments WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# Update
def update(appointment):
    sql = "UPDATE appointments SET (pet, appointment_date, check_in, check_out, vet) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [appointment.pet.id, appointment.appointment_date, appointment.check_in, appointment.check_out, appointment.vet.id, appointment.id]
    run_sql(sql, values)
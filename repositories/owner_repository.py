from db.run_sql import run_sql
from models.owner import Owner
from models.pet import Pet


def save(owner):
    sql = "INSERT INTO owners (name, phone_number, registration) VALUES (%s, %s, %s) RETURNING id"
    values = [owner.name, owner.phone_number, owner.registration]
    results = run_sql(sql, values)
    owner.id = results[0]['id']
    return owner


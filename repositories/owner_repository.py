from db.run_sql import run_sql
from models.owner import Owner
from models.pet import Pet


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
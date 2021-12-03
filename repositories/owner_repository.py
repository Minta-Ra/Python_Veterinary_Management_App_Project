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
    
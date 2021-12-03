from db.run_sql import run_sql
from models.vet import Vet


def save(vet):
    sql = "INSERT INTO vets (name, experience) VALUES (%s, %s) RETURNING id"
    values = [vet.name, vet.experience]
    results = run_sql(sql, values)
    vet.id = results[0]['id']
    return vet

def select_all():
    vets = []
    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    for row in results:
        vet = Vet(row['name'], row['experience'], row['id'])
        vets.append(vet)
    return vets

def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        vet = Vet(result['name'], result['experience'], result['id'])
    return vet

def delete_all():
    sql = "DELETE  FROM vets"
    run_sql(sql)
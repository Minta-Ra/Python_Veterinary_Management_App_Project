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
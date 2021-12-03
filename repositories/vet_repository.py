from db.run_sql import run_sql
from models.vet import Vet


def save(vet):
    sql = "INSERT INTO vets (name, experience) VALUES (%s, %s) RETURNING id"
    values = [vet.name, vet.experience]
    results = run_sql(sql, values)
    vet.id = results[0]['id']
    return vet
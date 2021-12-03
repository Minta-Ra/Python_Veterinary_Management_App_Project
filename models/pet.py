class Pet():
    def __init__(self, name, dob, pet_type, treatment_notes, vet, owner, id = None):
        self.name = name
        self.dob = dob
        self.pet_type = pet_type
        self.treatment_notes = treatment_notes
        self.vet = vet      # (FK)
        self.owner = owner  # (FK)
        self.id = id        # (PK)
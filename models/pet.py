class Pet():
    def __init__(self, name, dob, pet_type, owner, vet, treatment_notes, id = None):
        self.name = name
        self.dob = dob
        self.pet_type = pet_type
        self.owner = owner              # (FK)
        self.vet = vet                  # (FK)
        self.treatment_notes = treatment_notes
        self.id = id                    # (PK)
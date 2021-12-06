class Appointment():
    def __init__(self, pet, appointment_date, check_in, check_out, vet, id = None):
        self.pet = pet                  # (FK)
        self.appointment_date = appointment_date
        self.check_in = check_in
        self.check_out = check_out
        self.vet = vet                  # (FK)
        self.id = id                    # (PK)
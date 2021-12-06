import pdb
from controllers.appointment_controller import appointments
from models.appointment import Appointment
from models.vet import Vet
from models.owner import Owner
from models.pet import Pet
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository
import repositories.pet_repository as pet_repository
import repositories.appointment_repository as appointment_repository



vet_repository.delete_all()
owner_repository.delete_all()
pet_repository.delete_all()
appointment_repository.delete_all()


# Vets #####################################
vet_1 = Vet("Dr. Jake Smith", 6)
vet_repository.save(vet_1)

vet_2 = Vet("Dr. Rachel Johnson", 9)
vet_repository.save(vet_2)

vet_3 = Vet("Dr. Jane Miller", 14)
vet_repository.save(vet_3)

vet_4 = Vet("Dr. Craig Williams", 8)
vet_repository.save(vet_4)


# Owners ###################################
owner_1 = Owner("Joseph Jones", "+44 7425 563522", True)
owner_repository.save(owner_1)

owner_2 = Owner("Olivia Davis", "+44 7366 864434", False)
owner_repository.save(owner_2)

owner_3 = Owner("Samantha Thompson", "+44 7346 872625", False)
owner_repository.save(owner_3)

owner_4 = Owner("Liam Taylor", "+44 7755 766534", False)
owner_repository.save(owner_4)

owner_5 = Owner("Kyle Harris", "+44 7334 886423", True)
owner_repository.save(owner_5)

owner_6 = Owner("Augustine Evans", "+44 7487 755429", False)
owner_repository.save(owner_6)

owner_7 = Owner("Johnathan Roberts", "+44 7457 886535", True)
owner_repository.save(owner_7)


# # Pets #####################################
pet_1 = Pet("Layla", "2020-09-09", "Dog", owner_1, vet_3, "Ear drops needed to treat ear infection")
pet_repository.save(pet_1)
pet_2 = Pet("Mylo", "2016-04-26", "Cat", owner_1, vet_3, "Weekly spray from fleas")
pet_repository.save(pet_2)

pet_3 = Pet("Snoopy", "2018-02-12", "Rabbit", owner_2, vet_2, "Operation on teeth")
pet_repository.save(pet_3)

pet_4 = Pet("Bella", "2014-10-24", "Cat", owner_3, vet_4, "Eye drops to treat red eye")
pet_repository.save(pet_4)
pet_5 = Pet("Maya", "2015-06-18", "Dog", owner_3, vet_4, "Yearly flue vaccination")
pet_repository.save(pet_5)

pet_6 = Pet("Max", "2021-09-17", "Dog", owner_4, vet_1, "Vaccination from rabies")
pet_repository.save(pet_6)

pet_7 = Pet("Chase", "2017-12-10", "Ferret", owner_5, vet_1, "Different food to be suggested")
pet_repository.save(pet_7)

pet_8 = Pet("Teah", "2013-04-29", "Dog", owner_6, vet_2, "Pet passport to be issued")
pet_repository.save(pet_8)
pet_9 = Pet("Molly", "2014-08-20", "Cat", owner_6, vet_2, "Yearly check-up and vaccination")
pet_repository.save(pet_9)

pet_10 = Pet("Teddy", "2021-10-01", "Dog", owner_7, vet_3, "Prescribe puppy worming treatment")
pet_repository.save(pet_10)


# Appointments #############################
appointment_1 = Appointment(pet_1, "2021-12-12", "12:30", "12:45", vet_3)
appointment_repository.save(appointment_1)

appointment_2 = Appointment(pet_4, "2021-12-18", "16:00", "16:15", vet_4)
appointment_repository.save(appointment_2)

appointment_3 = Appointment(pet_5, "2021-12-18", "16:15", "16:35", vet_4)
appointment_repository.save(appointment_3)


############################################
all_vets = vet_repository.select_all()
all_owners = owner_repository.select_all()
all_pets = pet_repository.select_all()


# Print it out to see in terminal
for vet in all_vets:
    print(vet.__dict__)

for owner in all_owners:
    print(owner.__dict__)

for pet in all_pets:
    print(pet.__dict__)
############################################

pdb.set_trace()
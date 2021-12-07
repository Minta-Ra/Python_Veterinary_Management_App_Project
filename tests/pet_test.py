import unittest
from models.pet import Pet
from models.vet import Vet
from models.owner import Owner


class PetTest(unittest.TestCase):
    def setUp(self):
        self.vet_3 = Vet("Dr. Jane Miller", 14)
        self.owner_1 = Owner("Joseph Jones", "+44 7425 563522", True)
        self.pet_1 = Pet("Layla", "2020-09-09", "Dog", self.owner_1, self.vet_3, "Ear drops needed to treat ear infection")

    def test_pet_has_name(self):
        expected = "Layla"
        actual = self.pet_1.name
        self.assertEqual(expected, actual)

    def test_pet_has_owner(self):
        expected = "Joseph Jones"
        actual = self.pet_1.owner.name
        self.assertEqual(expected, actual)

    def test_pet_has_vet(self):
        expected = "Dr. Jane Miller"
        actual = self.pet_1.vet.name
        self.assertEqual(expected, actual)

    def test_pet_has_treathemt_notes(self):
        expected = "Ear drops needed to treat ear infection"
        actual = self.pet_1.treatment_notes
        self.assertEqual(expected, actual)
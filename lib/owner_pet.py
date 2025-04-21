class Pet:
    # Class variable to store all the pets
    all = []

    # Class variable to store the number of pets types
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner=None):
        #Validate Pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}.")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        # Add the instance to the class variable all
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        """Return a list of all pets owned by this owner."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Add a pet to this owner, ensuring the pet is of the type of the Pet"""
        if not isinstance(pet, Pet):
            raise Exception("add_pet() argument must be an instance of the Pet class.")

        pet.owner = self

    def get_sorted_pets(self):
        """Return a list of all owner's pets sorted by name."""
        return sorted(self.pets(), key=lambda pet: pet.name)
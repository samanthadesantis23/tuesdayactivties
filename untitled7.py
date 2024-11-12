# Define the Pet class
class Pet:
    def __init__(self, name, species, year_of_birth):
        self.name = name  # Name of the pet (string)
        self.species = species  # Species of the pet (string)
        self.year_of_birth = year_of_birth  # Year of birth of the pet (integer)

# Function to create and return a new Pet object
def new_pet(name: str, species: str, year_of_birth: int) -> Pet:
    # Create a new Pet object using the provided arguments
    pet = Pet(name, species, year_of_birth)
    return pet
# Create a new pet using the new_pet function
my_pet = new_pet("Whiskers", "Cat", 2016)

# Accessing and printing the attributes of the pet
print(f"My pet's name is {my_pet.name}.")
print(f"My pet is a {my_pet.species}.")
print(f"My pet was born in {my_pet.year_of_birth}.")

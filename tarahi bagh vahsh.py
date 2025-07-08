class Animal:
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

# نمونه شیر
lion = Animal("شیر", "Panthera leo", 5, "غُرغُر")
print(f"نام: {lion.name}")
print(f"گونه: {lion.species}")
print(f"سن: {lion.age}")
print(f"صدا: {lion.sound}")

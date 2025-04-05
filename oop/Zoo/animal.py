class Animal:
    def __init__(self, name, species, age, sound):
        """Initializes the animal object with name, species, age and sound"""
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self):
        """Prints the sound of the animal"""
        print(f"{self.name} says {self.sound}")

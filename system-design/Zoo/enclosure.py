class Enclosure:
    def __init__(self, name, max_capacity):
        """Initializes the enclosure object with name and max_capacity"""
        self.name = name
        self.max_capacity = max_capacity
        self.animals = []

    def add_animal(self, animal):
        """Adds the animal to the enclosure"""
        if len(self.animals) < self.max_capacity:
            self.animals.append(animal)
        else:
            print(f"{self.name} is full")

    def remove_animal(self, animal):
        """Removes the animal from the enclosure"""
        self.animals.remove(animal)

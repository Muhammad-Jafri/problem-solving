class Caretaker:
    def __init__(self, name, enclosure):
        """Initializes the caretaker object with name and enclosure"""
        self.name = name
        self.enclosure = enclosure

    def feed_animals(self):
        """Feeds all the animals in the enclosure"""

        feeding_print_statement = f"{self.name} is feeding the animals in {self.enclosure.name} that houses the following animals: \n"
        for animal in self.enclosure.animals:
            feeding_print_statement += f"\n{animal.name}"
        
        feeding_print_statement += "\n"
        print(feeding_print_statement)

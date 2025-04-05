from animal import Animal
from caretaker import Caretaker
from enclosure import Enclosure

if __name__ == "__main__":
    lion = Animal("Leo", "Lion", 5, "Roar")
    elephant = Animal("Ellie", "Elephant", 10, "Trumpet")
    monkey = Animal("Mike", "Monkey", 3, "Squeak")

    lion_enclosure = Enclosure("Lion Enclosure", 2)
    lion_enclosure.add_animal(lion)
    lion_enclosure.add_animal(elephant)

    monkey_enclosure = Enclosure("Monkey Enclosure", 1)
    monkey_enclosure.add_animal(monkey)

    caretaker = Caretaker("John", lion_enclosure)
    caretaker.feed_animals()

    caretaker.enclosure = monkey_enclosure
    caretaker.feed_animals()

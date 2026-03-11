from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
    @abstractmethod
    def action(self):
        pass


class Dog(Animal):
    def __init__(self):
        self.name = "Dog"
    def speak(self):
        print("Dog says: Woof! 🐶")
    def action(self):
        print("Dog runs in the yard.")


class Cat(Animal):
    def __init__(self):
        self.name = "Cat"
    def speak(self):
        print("Cat says: Meow! 🐱")
    def action(self):
        print("Cat climbs the tree.")


class Bird(Animal):
    def __init__(self):
        self.name = "Bird"
    def speak(self):
        print("Bird says: Tweet! 🐦")
    def action(self):
        print("Bird flies in the sky.")


class Fish(Animal):
    def __init__(self):
        self.name = "Fish"
    def speak(self):
        print("Fish says: Blub! 🐟")
    def action(self):
        print("Fish swims in the tank.")


class AnimalFactory:
    Animals = {
        "dog": Dog,
        "cat": Cat,
        "bird": Bird,
        "fish": Fish
    }
    def create_animal(self, animal_type):
        animal_class = self.Animals.get(animal_type.lower())
        if animal_class:
            return animal_class()
        else:
            print("Unknown animal.")


def main():
    while True:
        animal = input("Enter an animal (dog/cat/bird/fish) or 'q' to quit: ")
        if animal == "q":
            break
        factory = AnimalFactory()
        animal_obj = factory.create_animal(animal)
        if animal_obj:
            animal_obj.speak()
            animal_obj.action()
main()
"""
Animal SheltenAn animal shelter, which holds only dogs and cats, operates on a strictly "first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat.You may use the built-in LinkedList data structure.
"""

from collections import deque

class Animal:
    def __init__(self, name, order):
        self.name = name
        self.order = order  #(timestamp)

    def isOlderThan(self, other):
        return self.order < other.order

class Dog(Animal):
    def __init__(self, name, order):
        super().__init__(name, order)

class Cat(Animal):
    def __init__(self, name, order):
        super().__init__(name, order)

class AnimalShelter:
    def __init__(self):
        self.dogs = deque()
        self.cats = deque()
        self.order = 0

    def enqueue(self, animal):
        animal.order = self.order
        self.order += 1
        
        if isinstance(animal, Dog):
            self.dogs.append(animal)
        elif isinstance(animal, Cat):
            self.cats.append(animal)

    def dequeueAny(self):
        """
        Dequeue animal
        """
        if not self.dogs and not self.cats:
            return None 

        if not self.dogs: 
            return self.dequeueCat()
        if not self.cats:
            return self.dequeueDog()

        if self.dogs[0].isOlderThan(self.cats[0]):
            return self.dequeueDog()
        else:
            return self.dequeueCat()

    def dequeueDog(self):
        """
        Dequeue dog.
        """
        if self.dogs:
            return self.dogs.popleft()
        return None

    def dequeueCat(self):
        """
        Dequeue cat.
        """
        if self.cats:
            return self.cats.popleft()
        return None




# shelter = AnimalShelter()
# shelter.enqueue(Dog("Dog1", 0))
# shelter.enqueue(Cat("Cat1", 0))
# assert shelter.dequeueAny().name == "Dog1"
# assert shelter.dequeueAny().name == "Cat1"

# shelter = AnimalShelter()
# shelter.enqueue(Dog("Dog1", 0))
# shelter.enqueue(Cat("Cat1", 0))
# shelter.enqueue(Dog("Dog2", 0))
# assert shelter.dequeueDog().name == "Dog1"

# shelter = AnimalShelter()
# shelter.enqueue(Dog("Dog1", 0))
# shelter.enqueue(Cat("Cat1", 0))
# assert shelter.dequeueCat().name == "Cat1"

# shelter = AnimalShelter()
# shelter.enqueue(Dog("Dog1", 0))
# shelter.enqueue(Cat("Cat1", 0))
# assert shelter.dequeueAny().name == "Dog1"
# assert shelter.dequeueCat().name == "Cat1"

# shelter = AnimalShelter()
# assert shelter.dequeueAny() is None
# assert shelter.dequeueDog() is None
# assert shelter.dequeueCat() is None


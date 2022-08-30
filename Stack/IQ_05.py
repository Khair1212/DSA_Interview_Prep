# An animal shelter which holds only dogs and cats, operates on a strictly "first in, first out" basis. People must adopt either the "oldest"
# (based on the arriival time) of all animals at the shelter, or they can select wheather they would prefer a dog or a car (and will receve the oldest animal of that type).
# They cannot select which specific animal they would like. Create the data strcturess to maintain this system and implement operations such as enqueues, dequeueAny, dequeueDog, and dequeCat

class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, animal, type):
        if type == 'cat':
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeueCat(self):
        if len(self.cats) == 0:
            return None
        else:
            cat = self.cats.pop(0)
            return cat

    def dequeueDogs(self):
        if len(self.dogs) == 0:
            return None
        else:
            dog = self.dogs.pop(0)
            return dog

    def dequeueAny(self):
        if len(self.dogs) == 0 and len(self.cats) == 0:
            return None
        if len(self.cats) == 0:
            result = self.dogs.pop(0)
        else:
            result = self.cats.pop(0)
        return result


q = AnimalShelter()
q.enqueue('Cat1', 'cat')
q.enqueue('Cat2', 'cat')
q.enqueue('Dog1', 'dog')
q.enqueue('Dog2', 'dog')
print(q.dequeueDogs())
print(q.dequeueCat())
print(q.dequeueAny())
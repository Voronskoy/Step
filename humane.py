class Simulation:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def simulate(self):
        for person in self.people:
            person.speak()
            person.move()

class Person:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} говорит")

    def move(self):
        print(f"{self.name} двигается")


sim = Simulation()
person1 = Person("Влад")
person2 = Person("Егор")

sim.add_person(person1)
sim.add_person(person2)

sim.simulate()

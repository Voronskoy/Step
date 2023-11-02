class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.happiness = 0

    def feed(self):
        self.hunger += 1
        self.happiness += 1

    def play(self):
        self.happiness += 1

    def sleep(self):
        self.hunger += 1

    def check_status(self):
        print(f"{self.name}: Голод - {self.hunger}, Счастье - {self.happiness}")



cat = Cat("Сима")
cat.feed()
cat.play()
cat.check_status()

class Pet:
    # To prevent someone from trying to teach the pet a trick that doesn't exist
    # This is a class variable that contains a list of valid tricks
    valid_tricks = ["sit", "stay", "roll over", "play dead", "fetch", "shake", "high five", "spin"]

    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} had a yummy meal! 🍖")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} had a nice nap. 💤")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2 # Playing costs energy
            self.happiness = min(10, self.happiness + 2) # But playing makes the pet happy
            self.hunger = min(10, self.hunger + 1) # Playing makes the pet a bit hungry
            print(f"{self.name} played and had a blast! 🎾")
        else:
            print(f"{self.name} is too tired to play. 😴")

    def train(self, trick):
        if trick not in Pet.valid_tricks:
            print(f"❌ {trick} is not a valid trick for a dog!")
            print(f"Try one of these: {', '.join(Pet.valid_tricks)}")
            return

        if trick not in self.tricks:
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} learned a new trick: {trick}! 🐕‍🦺")
        else:
            print(f"{self.name} already knows how to {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")

    def get_status(self):
        print(f"📋 Status of {self.name}:")
        print(f"  Hunger: {self.hunger}/10")
        print(f"  Energy: {self.energy}/10")
        print(f"  Happiness: {self.happiness}/10")
        print()


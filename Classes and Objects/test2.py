

#parent class
class Organism:
    name = "unknown"
    species = "unknown"
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "unknown"
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg

#child class
class Human(Organism):
    name = "Bill"
    species = "Homosapien"
    legs = 2
    arms = 2
    origin = "Earth"

    def ingenuity(self):
        msg = "\nCreate a weapon using only a paper clip, chewing gum and a roll of toilet paper!"
        return msg

#another child class
class Dog(Organism):
    name = "Spike"
    species = "Canine"
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = "Earth"

    def bark(self):
        msg = "\nWOOF WOOF!"
        return msg

#another child class
class Bacterium(Organism):
    name = "X"
    species = "Bacteria"
    legs = 0
    arms = 0
    dna = "Sequence Q"
    origin = "Mars"

    def replicate(self):
        msg = "\nThe cells begin to divide and multiply into two seperate organisms!"
        return msg
        



if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bark())

    bacterium = Bacterium()
    print(Bacterium().information())
    print(Bacterium().replicate())

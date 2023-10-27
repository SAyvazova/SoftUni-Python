class Zoo:

    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        info_list = []
        capitalized_species = ""
        if species == "mammal":
            info_list = self.mammals
            capitalized_species = "Mammals"
        elif species == "fish":
            info_list = self.fishes
            capitalized_species = "Fishes"
        elif species == "bird":
            info_list = self.birds
            capitalized_species = "Birds"

        return f"{capitalized_species} in {self.name}: {', '.join(info_list)}\nTotal animals: {Zoo.__animals}"


name_zoo = input()
zoo = Zoo(name_zoo)
nr_animals = int(input())
for _ in range(nr_animals):
    species, name = input().split()
    zoo.add_animal(species, name)

specific_species = input()
print(zoo.get_info(specific_species))

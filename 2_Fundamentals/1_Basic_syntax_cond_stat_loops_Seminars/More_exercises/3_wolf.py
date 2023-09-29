queue = input()
queue_as_list = list(queue.split(", "))
nr_animals = len(queue_as_list)

for index in range(nr_animals - 1, -1, -1):
    animal = queue_as_list[index]
    if animal == "wolf":
        if index == nr_animals - 1:
            print("Please go away and stop eating my sheep")
            break
        else:
            print(f"Oi! Sheep number {nr_animals - (index + 1)}! You are about to be eaten by a wolf!")
            break




info = input()
phonebook = {}

while not info.isnumeric():
    name, number = info.split("-")
    phonebook[name] = number
    info = input()

nr_searches = int(info)
for _ in range(nr_searches):
    search_name = input()
    if search_name in phonebook:
        search_number = phonebook[search_name]
        print(f"{search_name} -> {search_number}")
    else:
        print(f"Contact {search_name} does not exist.")

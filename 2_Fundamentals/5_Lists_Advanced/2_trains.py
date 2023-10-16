train = [0] * int(input())
command = input()
while command != "End":
    command_parts = command.split()
    action = command_parts[0]
    if action == "add":
        nr_people = int(command_parts[1])
        train[-1] += nr_people
    elif action == 'insert':
        index = int(command_parts[1])
        nr_people = int(command_parts[2])
        train[index] += nr_people
    elif action == 'leave':
        index = int(command_parts[1])
        nr_people = int(command_parts[2])
        train[index] -= nr_people
    command = input()

print(train)
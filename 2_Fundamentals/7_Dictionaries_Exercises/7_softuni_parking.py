nr_cars = int(input())
registered_users = {}

for _ in range(nr_cars):
    raw_data = input().split()
    command = raw_data[0]
    username = raw_data[1]
    if command == "register":
        license_plate_number = raw_data[2]
        if username in registered_users:
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            registered_users[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    elif command == "unregister":
        if username in registered_users:
            del registered_users[username]
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

for username, license_plate_number in registered_users.items():
    print(f"{username} => {license_plate_number}")

USERNAME = input()
PASSWORD = input()

while True:
    password = input()
    if password == PASSWORD:
        print(f"Welcome {USERNAME}!")
        break

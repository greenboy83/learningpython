import random

print("a =", random.randint(1, 6))

username = ""
password = ""

while not username:
    username = input("Please enter username:")

while not password:
    password = input("Password:")

if not (username == "Bill" and password == "123"):
    print("Hi Bill, what's up?")
else:
    print("Login failed.")

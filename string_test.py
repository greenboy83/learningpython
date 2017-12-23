import random

word = "game"


chest1 = ("a", "b", "c")
chest2 = ("d", "e")

chest3 = chest1 + chest2
print(chest3)

choice = random.choice(chest3)

print(choice)




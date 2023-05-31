import random

names = input("Enter the names of everyone around: ").split(",")
# rand = random.randint(0, len(names) - 1)
# print(f"{names[rand]} will pay the bill")
payer = random.choice(names)
print(f"{payer} will pay the bill")



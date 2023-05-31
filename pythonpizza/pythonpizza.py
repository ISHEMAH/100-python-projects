smallpizza = 15
mediumpizza = 20
largepizza = 25

pepperonis = 2
pepperoniml = 3

cheese = 1

print("Welcome to python Pizza Deliveries :)")
size = input("Enter the size of the pizza(small,medium,large): ").lower()
addpepperoni = input("Do you want pepperoni (yes aro no): ").lower()
extracheese = input("Do you want extra cheese (yes or no): ").lower()

if size == "small":
    price = smallpizza
    if addpepperoni == "yes":
        price += pepperonis
    else:
        pass
    if extracheese == "yes":
        price += cheese
    else:
        pass
    print(f"The total price is {price}$ ")
elif size == "medium":
    price = mediumpizza
    if addpepperoni == "yes":
        price += pepperoniml
    else:
        pass
    if extracheese == "yes":
        price += cheese
    else:
        pass
    print(f"The total price is {price}$ ")
elif size == "large":
    price = largepizza
    if addpepperoni == "yes":
        price += pepperoniml
    else:
        pass
    if extracheese == "yes":
        price += cheese
    else:
        pass
    print(f"The total price is {price}$ ")

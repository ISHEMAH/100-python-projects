print("Welcome to Treasure Game🏴‍☠️\nYou mission is to find the treasure\n")
cross = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"").lower()
if cross == "left":
    boat = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat.Type \"swim\" to swim across\n").lower()
    if boat == "wait":
        door = input("You arrive at the island unharmed. There is house with 3 doors One red, on yellow and one blue. Which colour do you choose?").lower()
        if door == "yellow":
            print("🏆Congratulations you found the treasure🏆")
        elif door == "red" or door == "blue":
            print("Game over,wrong door")
    elif boat == "swim":
        print("Game over")
elif cross == "right":
    print("Game over")

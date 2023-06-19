name1 = input("enter the first name: ").lower()
name2 = input("Enter the second name: ").lower()
combination = name1 + name2
step1 = combination.count("t") + combination.count("r") + combination.count("u") + combination.count("e")
step2 = combination.count("l") + combination.count("o") + combination.count("v") + combination.count("e")

percent = f"{step1}{step2}"

if 10 <= int(percent) >= 90:
    print(f"Your score is {percent}%, you go together like coke and mentos")
elif 40 <= int(percent) <= 50:
    print(f"Your score is {percent}% ,you are alright together")
else:
    print(f"Your score is {percent}% ")





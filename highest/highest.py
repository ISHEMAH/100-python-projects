numbers = input("Enter the numbers").split()

for n in range(0, len(numbers)):
    numbers[n] = int(numbers[n])

great = numbers[0]

for number in numbers:
    if great < number:
        great = number

print(f"the maximum is {great}")



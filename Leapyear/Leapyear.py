year = int(input("Enter the year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a Leap year 366 Days")
        else:
            print(f"{year} is an ordinary year 365 Days")
    else:
        print(f"{year} is a Leap year 366 Days")
else:
    print(f"{year} is an ordinary year 365 Days")

heights = input("Enter the heights of the students").split()
summ = 0
count = 0
for n in range(0, len(heights)):
    heights[n] = int(heights[n])


for height in heights:
    summ += height
    count += 1

avg = summ/count

print(f"The average is {avg}")

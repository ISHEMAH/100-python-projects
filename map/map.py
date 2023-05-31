row1 = ["🟥", "🟥", "🟥"]
row2 = ["🟥", "🟥", "🟥"]
row3 = ["🟥", "🟥", "🟥"]

rows = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = int(input("Enter the the position of the treasure(columnrow): "))
col = int(position / 10) - 1
row = int(position % 10) - 1
rows[row][col] = "🏆"
print(f"{row1}\n{row2}\n{row3}")
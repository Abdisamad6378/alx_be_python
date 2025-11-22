"""Draw a pattern using nested loops."""

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

print(f"Creating a {size}x{size} pattern:\n")

row = 0
while row < size:
    col = 0
    while col < size:
        print("*", end=" ")
        col += 1
    print()  # New line after each row
    row += 1

print(f"\nDone! Created a {size} row by {size} column square.")
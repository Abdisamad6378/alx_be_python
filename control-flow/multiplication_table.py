"""Generate and display a multiplication table for a given number."""

number = int(input("Enter a number to see its multiplication table:"))
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    result = i * number
    print(f"{number} * {i} = {result}")

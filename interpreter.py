# Step 1: Get user input
user_input = input("Enter an arithmetic expression: ").strip()

# Step 2: Parse the input
num1, operator, num2 = user_input.split()

# Step 3: Perform the calculation
num1 = float(num1)
num2 = float(num2)
result = 0

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero")
        exit()

# Step 4: Display the result
print(f"Result: {result}")

"""A simple beginner-friendly calculator."""


# Ask the user for the first number and convert it to a decimal number.
try:
    first_number = float(input("Enter first number: "))

    # Ask the user which arithmetic operation to perform.
    operator = input("Enter operator (+, -, *, /): ")

    # Ask the user for the second number.
    second_number = float(input("Enter second number: "))

    # Perform the operation selected by the user.
    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        # Division by zero is not allowed in arithmetic.
        if second_number == 0:
            print("\nError: Cannot divide by zero.")
        else:
            result = first_number / second_number
            print(f"\nResult: {first_number:g} {operator} {second_number:g} = {result:g}")
    else:
        # Tell the user when the operator is not supported.
        print("\nError: Invalid operator. Please use +, -, *, or /.")

    # Display the result for operations other than division.
    if operator in ("+", "-", "*"):
        print(f"\nResult: {first_number:g} {operator} {second_number:g} = {result:g}")
except ValueError:
    # Handle values that cannot be converted to numbers.
    print("\nError: Please enter a valid number.")
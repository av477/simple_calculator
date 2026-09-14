def addition(first_number, second_number):
    return first_number + second_number


def subtraction(first_number, second_number):
    return first_number - second_number


def multiplication(first_number, second_number):
    return first_number * second_number


def division(first_number, second_number):
    if second_number == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return first_number / second_number


def calculator():
    print("Simple Calculator For Basis Mathematics Operations")
    print("1. Enter 1 for Addition")
    print("2. Enter 2 for Subtraction")
    print("3. Enter 3 for Multiplication")
    print("4. Enter 4 for Division")
    print("5. Enter 5 to Exit")

    while True:
        choice = input("Choose an operation between (1-5): ")

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice. Please enter a number from 1 to 5.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        try:
            if choice == "1":
                result = addition(num1, num2)
                print(f"Result: {result}")
            elif choice == "2":
                result = subtraction(num1, num2)
                print(f"Result: {result}")
            elif choice == "3":
                result = multiplication(num1, num2)
                print(f"Result: {result}")
            elif choice == "4":
                result = division(num1, num2)
                print(f"Result: {result}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    calculator()

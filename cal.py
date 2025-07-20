import math

def basic_calculator():
    print("\nChoose operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Square root (√)")
    print("6. Power (x^y)")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")
    print("0. Exit")

    while True:
        choice = input("\nEnter choice (0-9): ")

        if choice == '0':
            print("Calculator closed.")
            break

        elif choice in ['1', '2', '3', '4', '6']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", num1 + num2)
            elif choice == '2':
                print("Result:", num1 - num2)
            elif choice == '3':
                print("Result:", num1 * num2)
            elif choice == '4':
                if num2 != 0:
                    print("Result:", num1 / num2)
                else:
                    print("Error: Cannot divide by zero.")
            elif choice == '6':
                print("Result:", math.pow(num1, num2))

        elif choice == '5':
            num = float(input("Enter number: "))
            if num >= 0:
                print("Result:", math.sqrt(num))
            else:
                print("Error: Cannot find square root of negative number.")

        elif choice in ['7', '8', '9']:
            angle = float(input("Enter angle in degrees: "))
            rad = math.radians(angle)
            if choice == '7':
                print("sin(", angle, ") =", math.sin(rad))
            elif choice == '8':
                print("cos(", angle, ") =", math.cos(rad))
            elif choice == '9':
                print("tan(", angle, ") =", math.tan(rad))

        else:
            print("Invalid input. Please enter a valid choice.")

# Run the calculator
basic_calculator()

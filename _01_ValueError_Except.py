try:
    number = int(input("Enter an integer: "))
    print("You entered:", number)
except ValueError:
    print("Error: Invalid input. Please enter an integer.")

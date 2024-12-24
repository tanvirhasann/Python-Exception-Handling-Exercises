my_list = [1, 2, 3, 4, 5]
try:
    index = int(input("Enter an index: "))
    print("Element:", my_list[index])
except IndexError:
    print("Error: Index out of range.")

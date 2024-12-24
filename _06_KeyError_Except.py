my_dict = {"a": 1, "b": 2, "c": 3}
try:
    key = input("Enter a key: ")
    print("Value:", my_dict[key])
except KeyError:
    print("Error: Key not found in dictionary.")

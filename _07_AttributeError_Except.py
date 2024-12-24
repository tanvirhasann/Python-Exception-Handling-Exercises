try:
    my_list = [1, 2, 3]
    my_list.append(4)  # Valid
    my_list.sort()  # Valid
    my_list.invalid_method()  # Invalid
except AttributeError:
    print("Error: Object does not have this attribute.")

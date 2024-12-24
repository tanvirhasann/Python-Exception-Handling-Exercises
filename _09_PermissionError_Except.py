try:
    with open("restricted_file.txt", "w") as file:
        file.write("Testing permission error.")
except PermissionError:
    print("Error: You do not have permission to write to this file.")

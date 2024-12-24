import time

try:
    raise TimeoutError("The operation timed out.")  # Simulating a timeout
except TimeoutError as e:
    print("Error:", e)

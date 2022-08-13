from cs50 import get_int

# Get Input from User
while True:
    height = get_int("Height of the Pyramid: ")
    if 1 <= height <= 8:
        break

# Print the Pyramid
for i in range(height):
    print(" " * (height - (i + 1)), end="")
    print("#" * (i + 1))
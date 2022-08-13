from cs50 import get_string
from cs50 import get_int

# Get the Credit Card Number as a String
number = get_string("Number: ")

# Implement Chekcsum Algorithm
def checksum(number):
    c = 0

    # Check Length
    if not (13 <= len(number) <= 16):
        return False

    if len(number) == 15:
        return amex(number)

    for i in range(len(number) - 2, -1, -2):
        x = int(number[i]) * 2
        if (x < 10):
            c += x
        elif x >= 10:
            for digits in str(x):
                c += int(digits)

    for j in range(len(number) - 1, 0, -2):
        c += int(number[j])

    if str(c)[-1] == "0":
        return True
    else:
        return False


def amex(number):
    c = 0

    for i in range(len(number) - 2, 0, -2):
        x = int(number[i]) * 2
        if (x < 10):
            c += x
        elif x >= 10:
            for digits in str(x):
                c += int(digits)

    for j in range(len(number) - 1, -1, -2):
        c += int(number[j])
    return c

# Boolean Value
valid = checksum(number)

if valid:
    if len(number) == 15 and (number[:2] in ["34", "37"]):
        print("AMEX")
    elif len(number) == 16 and (number[:2] in ["51", "52", "53", "54", "55"]):
        print("MASTERCARD")
    elif (len(number) == 13 or len(number) == 16) and (number[0] == "4"):
        print("VISA")
    else:
        print("NOTHING")
else:
    print("INVALID")
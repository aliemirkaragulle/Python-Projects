from cs50 import get_float

# Get Input from User
while True:
    change = get_float("Change owed: ")
    if change > 0:
        break

# Amounts of Money
quarters = 0.25
dimes = 0.10
nickels = 0.05
pennies = 0.01

# Calculating Changes per Type of Money


def quarters_sum(change, quarters):
    return change // quarters


def dimes_sum(change, dimes):
    return change // dimes


def nickels_sum(change, nickels):
    return change // nickels


def pennies_sum(change, pennies):
    return change // pennies


# Minimum Change Amount
def total_change(change):
    quarters_total = quarters_sum(change, quarters)
    change = change - (quarters * quarters_total)
    change = float("{0:.2f}".format(change))

    dimes_total = dimes_sum(change, dimes)
    change = change - (dimes * dimes_total)
    change = float("{0:.2f}".format(change))

    nickels_total = nickels_sum(change, nickels)
    change = change - (nickels * nickels_total)
    change = float("{0:.2f}".format(change))

    pennies_total = pennies_sum(change, pennies)

    return quarters_total + dimes_total + nickels_total + pennies_total


# Printing the Result
res = int(total_change(change))
print(f"{res}")
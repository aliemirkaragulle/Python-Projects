# Mario Bricks
def main():
    try:
        num = int(input("Size of the Structures: "))
    except:
        print("Enter an Integer!")
    else:
        
        mario_row(num)
        print("\n")

        mario_column(num)
        print("\n")

        mario_square(num)
        print("\n")

        mario_right_skewed_triangle(num)
        print("\n")

        mario_left_skewed_triangle(num)
        print("\n")



def mario_row(size):
    print("?" * size)



def mario_column(size):
    for _ in range(size):
        print("#")



def mario_square(size):

    # For each row in square
    for i in range(size):

        # For each brick in row
        for j in range(size):

            # Print brick
            print("#", end = "")
        
        # Print blank line
        print()



def mario_right_skewed_triangle(size):
    for i in range(size):
        for j in range(i + 1):
            print("#", end = "")
        print()



def mario_left_skewed_triangle(size):
    for i in range(size):
        for j in range(size - (i + 1)):
            print(" ", end = "")
        for k in range(i + 1):
            print("#", end = "")
        print()

if __name__ == "__main__":
    main()
# TODO
def main():
    height = get_height()
    # Iterate through each row
    for row in range(height):
        # Print spaces
        for i in range(height - row - 1, 0, -1):
            print(" ", end="")
        for i in range(row + 1):
            print("#", end="")
        print("  ", end="")
        for i in range(row + 1):
            print("#", end="")
        # Move to the next line
        print()


def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if 1 <= n <= 8:
                break
        except ValueError:
            print("That's not an integer!")
    return n


if __name__ == "__main__":
    main()

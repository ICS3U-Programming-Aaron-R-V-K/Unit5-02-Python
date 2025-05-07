# !/usr/bin/env python3
# Created By: Aaron Rivelino
# Date: May 7, 2025
# The program has a function that calculates the area of a triangle
# It will accept 2 parameters, base and height


# Function with two parameters to calculate area of a triangle
def calc_area(base, height):
    area = 0.5 * base * height
    print(f"The area of the triangle is {area:.2f} cm²")


# Main function to get the input and call the function
def main():

    # Get the user input as a string
    base_str = input("Enter the base of the triangle (cm): ")
    height_str = input("Enter the height of the triangle (cm): ")

    # Try catch for invalid input
    try:
        # type cast from string to float
        base = float(base_str)
        height = float(height_str)

        # If statement for getting only positive numbers
        if base <= 0 and height <= 0:
            print("Base and height must be positive numbers.")
        else:
            # If they are positive numbers call the function
            calc_area(base, height)

    # Exception for invalid input
    except Exception:
        print("Invalid input. Please enter a number")


if __name__ == "__main__":
    main()

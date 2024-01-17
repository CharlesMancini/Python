import math
from colorama import Fore


def triangle():
    base = float(input(Fore.BLUE + "Enter the base of the" + Fore.GREEN + " triangle: "))
    height = float(input(Fore.BLUE + "Enter the height of the" + Fore.GREEN + "  triangle: "))
    return base * height / 2


def rectangle():
    base = float(input(Fore.BLUE + "Enter the base of the " + Fore.RED + " rectangle: "))
    height = float(input(Fore.BLUE + "Enter the height of the " + Fore.RED + " rectangle: "))
    return base * height


def square():
    side = float(input(Fore.BLUE + "Enter the side of the " + Fore.YELLOW + " square: "))
    return side * side


def circle():
    radius = float(input(Fore.BLUE + "Enter the radius of the " + Fore.CYAN + " circle: "))
    return math.pi * (radius ** 2)


def main():
    while True:
        shape = input(Fore.BLUE + "Enter the name or first letter of the shape: " + Fore.GREEN + "(triangle, " +
                      Fore.RED + "rectangle, " + Fore.CYAN + " circle" + Fore.BLUE + " or " + Fore.YELLOW +
                      "square):")

        if shape == "t" or shape == "triangle":
            area = triangle()
        elif shape == "r" or shape == "rectangle":
            area = rectangle()
        elif shape == "c" or shape == "circle":
            area = circle()
        elif shape == "s" or shape == "square":
            area = square()
        else:
            print(Fore.RED + "Invalid shape entered.")
            continue

        print(Fore.GREEN + "The area is:", Fore.RED + str(area))
        again = input("Do you want to calculate another shape? (yes/no): ")
        if again.lower() != "yes" or again.lower() != "y":
            break

main()

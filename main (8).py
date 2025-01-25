import math

def CircleS(R):
    """
    Calculates the area of a circle with radius R.
    :param R: float, radius of the circle
    :return: float, area of the circle
    """
    return 3.14 * R ** 2

def calculate_areas(radii):
    """
    Calculates the areas for a list of radii.
    :param radii: list of float, radii of circles
    :return: list of float, areas of circles
    """
    return [CircleS(r) for r in radii]

def main():
    """
    Main function to input radii, calculate areas, and display results.
    """
    print("Enter the radii of three circles (separated by spaces):")
    radii = list(map(float, input().split()))

    if len(radii) != 3:
        print("Error: You must enter exactly three radii.")
        return

    areas = calculate_areas(radii)

    print("\nResults:")
    for i, area in enumerate(areas, 1):
        print(f"Circle {i}: Radius = {radii[i-1]}, Area = {area:.2f}")

if __name__ == "__main__":
    main()

"""Module to calculate the area of a circle."""

def area_of_circle(radius):
    """
    Calculate the area of a circle.

    Args:
        radius (float): Radius of the circle.

    Returns:
        float: Area of the circle.
    """
    pi = 3.14
    return pi * radius * radius


def main():
    """Main function to print area of a circle with radius 10."""
    r = 10
    area = area_of_circle(r)
    print(area)


if __name__ == "__main__":
    main()
#***************************************
def find_max_min(data):
    """
    Finds the maximum and minimum values in a list of numbers.

    Args:
        data: A list of numbers.

    Returns:
        A tuple containing the maximum and minimum values, or (None, None) if the list is empty.
    """
    if not data:
        return (None, None)

    maximum = data[0]
    minimum = data[0]
    for number in data:
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number
    return (maximum, minimum)

# Example usage
numbers = [5, 2, 9, 1, 5, 6]
max_val, min_val = find_max_min(numbers)

print(f"Maximum value: {max_val}")
print(f"Minimum value: {min_val}")

# another example:
def greet(name):
    """
    Greets a person with the given name.

    Args:
        name: The name of the person.
    """
    print(f"Hello, {name}!")

# Example usage:
greet("Alice")

# example using any():
def check_even(numbers):
    """
    Checks if any number in a list is even.

    Args:
        numbers: A list of numbers.

    Returns:
        True if at least one number is even, False otherwise.
    """
    return any(number % 2 == 0 for number in numbers)

# Example usage:
numbers1 = [1, 3, 5, 7]
numbers2 = [1, 2, 3, 4]

print(f"List 1 has an even number: {check_even(numbers1)}")
print(f"List 2 has an even number: {check_even(numbers2)}")
def sum_numbers(numbers):
    """Return the sum of a list of numbers."""
    total = 0
    for num in numbers:
        total += num
    return total


# Example usage
if __name__ == "__main__":
    result = sum_numbers([1, 2, 3, 4, 5])
    print(f"Sum: {result}")
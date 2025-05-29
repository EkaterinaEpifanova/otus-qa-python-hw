"""This module provides a function to calculate the average of a list of numbers."""
def calculate_average(numbers):
    """Return the average of a list of numbers."""
    total = sum(numbers)
    count = len(numbers)
    return total / count

nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)

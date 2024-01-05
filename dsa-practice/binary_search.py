def binary_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    """
    first = 0
    last = len(list) - 1
    while first <= last:
        midpoint = (first + last) // 2  # Floor division to round down to nearest whole number
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        elif list[midpoint] > target:
            last = midpoint - 1
    return None

def verify(index):
    if index is not None:
        print("Target found at index", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 11)
verify(result)

result = binary_search(numbers, 1)
verify(result)

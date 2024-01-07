def merge_sort(list):
    """
    Sorts a list in ascending order in O(kn log n), and returns it as a new list.
    First, finds the midpoint of the list and divides the list into sublists until each list is one element long.
    Then, recursively sorts the sublists.
    Finally, merges the sorted sublists.
    """
    if len(list) <= 1:
        return list

    # Divide
    left_half, right_half = split(list)

    # Sort
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    # Merge
    return merge(left, right)

def split(list):
    """
    Divides a list at its midpoint into two sublists.
    """
    midpoint = len(list) // 2
    left = list[:midpoint]
    right = list[midpoint:]

    return left, right

def merge(left, right):
    """
    Merges two lists into one.
    """
    merged_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1

    while i < len(left):
        merged_list.append(left[i])
        i += 1

    while j < len(right):
        merged_list.append(right[j])
        j += 1

    return merged_list

list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
sorted_list = merge_sort(list)
print(sorted_list)

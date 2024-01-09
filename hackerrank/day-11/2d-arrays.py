arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

def fetch_hourglass(arr, row_offset, col_offset):
    a = arr[row_offset][col_offset]
    b = arr[row_offset][col_offset + 1]
    c = arr[row_offset][col_offset + 2]
    d = arr[row_offset + 1][col_offset + 1]
    e = arr[row_offset + 2][col_offset]
    f = arr[row_offset + 2][col_offset + 1]
    g = arr[row_offset + 2][col_offset + 2]

    return [a, b, c, d, e, f, g]

def sum_hourglass(hourglass):
    hourglass_sum = 0
    for number in hourglass:
        hourglass_sum += number
    return hourglass_sum

max_hourglass_sum = float('-inf')
for i in range(5):
    row_offset = i
    for j in range(5):
        col_offset = j
        try:
            hourglass = fetch_hourglass(arr, row_offset, col_offset)
        except IndexError:
            # Not a valid hourglass shape
            continue
        sum = sum_hourglass(hourglass)
        if sum > max_hourglass_sum:
            max_hourglass_sum = sum

print(max_hourglass_sum)

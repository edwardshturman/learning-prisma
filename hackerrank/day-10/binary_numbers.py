def decimal_to_binary(n):
    quotient = n // 2
    remainder = str(n % 2)

    while quotient != 0:
        remainder += str(quotient % 2)
        quotient //= 2

    binary = remainder[::-1]

    return binary

def max_consecutive(string):
    consecutive = 0
    max = 0
    while string != '':
        if string[0] == '1':
            consecutive += 1
        elif string[0] == '0':
            consecutive = 0
        if consecutive > max:
            max = consecutive
        string = string[1:]

    return max

if __name__ == '__main__':
    n = int(input().strip())
    binary = decimal_to_binary(n)
    print(max_consecutive(binary))

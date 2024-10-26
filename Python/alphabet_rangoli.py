def get_alphabet(n):
    if 1 <= n <= 26:
        return chr(n + 96)
    else:
        raise ValueError(f"{n} is invalid number should be in range [1-26]")

def print_rangoli(size):
    for i in range(size):

        for j in range(2 * (size - i) - 2):
            print("-", end="")

        for j in range(i + 1):
            k = size - j
            print(get_alphabet(k), end="")
            if j < i:
                print("-", end="")
        while k < size:
            print("-", end="")
            print(get_alphabet(k + 1), end="")
            k += 1

        for j in range(2 * (size - i) - 2):
            print("-", end="")
        print()

    for i in range(size - 2, -1, -1):

        for j in range(2 * (size - i) - 2):
            print("-", end="")

        for j in range(i + 1):
            k = size - j
            print(get_alphabet(k), end="")
            if j < i:
                print("-", end="")
        while k < size:
            print("-", get_alphabet(k + 1), sep="", end="")
            k += 1

        for j in range(2 * (size - i) - 2):
            print("-", end="")
        print()


# main part
if __name__ == "__main__":
    n = int(input("Enter a number in range [1-26]: "))
    print_rangoli(n)
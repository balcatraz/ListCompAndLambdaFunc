def main():
    remainder = lambda num: num % 2

    print(remainder(3))

    product = lambda x, y: x * y

    print(product(2, 3))

    result10 = testFunc(10)
    result100 = testFunc(100)

    print(result10)
    print(result100)

    print(result100(2))
    print(result10(9))

    mydoubler = myFunct2(2)
    mytripler = myFunct2(3)

    print(mydoubler(11))
    print(mytripler(11))

    numbered_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]

    filtered_list = list(filter(lambda num: (num > 7), numbered_list))

    print(filtered_list)

    numbers = [1, 2, 3, 4]
    result = map(addition, numbers)

    print(list(result))

    result = list(map(lambda n: addition(n) + n, numbers))
    print(result)

    import os

    clear = lambda: os.system("cls")
    clear()


def testFunc(num):
    print(num)
    return lambda x: x * num


def myFunct2(n):
    return lambda a: a * n


def addition(n):
    return n + n


main()

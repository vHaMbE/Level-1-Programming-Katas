def hello(first_name):
    print(first_name)


hello("Vhambelani")


def even_or_odd(num):
    if num % 2 != 0:
        print("odd")
    else:
        print("even")


even_or_odd(6)


def square(num):
    for x in range(0, num):
        for y in range(0, num):
            print("#", end="")
        print("", end="\n")


square(2)


def triangle(num):
    for x in range(0, num):
        for y in range(0, x + 1):
            print("#", end="")
        print("", end="\n")


triangle(5)


def isosceles(num):
    z = 0
    for x in range(1, num + 1):
        for y in range(1, (num - x) + 1):
            print(end=" ")
        while z != (2 * x - 1):
            print("#", end="")
            z += 1
        z = 0
        print()


isosceles(4)


def longest(list):
    temp = len(list[0])
    longest = ""
    longest_list = []
    longest = max(list, key=len)
    print(longest)
    for y in range(len(list)):
        if len(list[y]) == len(longest):
            longest_list.append(list[y])
    print(longest_list)


longest(["once", "upon", "a", "time"])


def new_list(list1, list2):
    list = []
    for item1, item2 in zip(list1, list2):
        list.append(item1)
        list.append(item2)
    return list


x = new_list([11, 22, 33], [1, 2, 3])
print(x)

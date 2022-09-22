def function1(i, num):
    line = ""
    for j in range(1, i):
        line = line + str(num) + " "  # print     #(2 )
        num = num * 2                             #(2 4 )
    return line


def main():
    i = 0
    while i <= 6:
        print(function1(i, 2))
        i += 1


main()



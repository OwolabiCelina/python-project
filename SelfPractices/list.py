def two_sum(arr: list, target: int) -> list:
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]

    # return [-1, -1]


print(two_sum([3, -1, 5, 4], 8))


def balance_pair(brackets: str):
    if brackets.strip() == "" or len(brackets) % 2 == 1:

        return False

    stack: list = []

    for bracket in brackets:
        if bracket in "{[(":
            stack.append(bracket)

        elif bracket in ")]}":
            peek = stack[-1]

            if peek == "{" and bracket == "}":
                stack.pop()
            elif peek == "[" and bracket == "]":
                stack.pop()
            elif peek == "(" and bracket == ")":
                stack.pop()

        else:
            return False

    return True


new_bracket = "()"
print(balance_pair(new_bracket))

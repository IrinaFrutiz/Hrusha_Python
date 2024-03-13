from colorama import Fore

parenthesis_pair = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}


def check_regular_bracket_sequence(sequence):
    stack = []
    for i, char in enumerate(sequence):
        stack.append((char, i))
    stack = adjacent_element(stack)
    if stack:
        stack = start_end(stack)
    index = 0
    print("Ваша скобочная последовательность НЕ является правильной" if stack else "Ваша скобочная последовательность "
                                                                                   "Правильная")
    for i in stack:
        print(Fore.GREEN + userSequence[index: i[1]], end="")
        index = i[1] + 1
        print(Fore.RED + userSequence[i[1]], end="")
    print(Fore.GREEN + userSequence[index:])


def start_end(stack):
    try:
        if parenthesis_pair[stack[0][0]] == stack[-1][0]:
            stack.pop(0)
            stack.pop(-1)
            start_end(stack)
    except KeyError:
        return stack
    return stack


def adjacent_element(stack, k=0):
    try:
        if parenthesis_pair[stack[k][0]] == stack[k + 1][0]:
            stack.pop(k)
            stack.pop(k)
            adjacent_element(stack)
        else:
            adjacent_element(stack, k + 1)
    except KeyError:
        adjacent_element(stack, k + 1)
    except IndexError:
        return stack
    return stack


print("Обрабатываемые символы: {, }, [, ], ), (, <, >.", "Непарные и необрабатываемые символы в последовательности "
                                                         "будут отмечены красным. ", sep="\n")
print("Пример из задания: [((())()(())]]")
userSequence = input("Введите скобочную последовательность для проверки на правильность: ")
check_regular_bracket_sequence(userSequence)

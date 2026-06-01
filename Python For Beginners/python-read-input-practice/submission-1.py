def add_two_numbers() -> int:
    user_input = input()
    int_list = [int(s) for s in user_input.split(',')]
    total = 0
    for i in int_list:
        total += i
    return total


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())

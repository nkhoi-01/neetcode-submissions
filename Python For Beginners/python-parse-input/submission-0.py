from typing import List

def read_integers() -> List[int]:
    user_input = input()
    integer_list = [int(s) for s in user_input.split(',')]
    return integer_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())

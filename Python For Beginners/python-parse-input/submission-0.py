from typing import List


def read_integers() -> List[int]:
    userInput = input()
    retList = userInput.split(",")
    int_list = []

    for i,value in enumerate(retList):
        int_list.append(int(value))

    return int_list


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())

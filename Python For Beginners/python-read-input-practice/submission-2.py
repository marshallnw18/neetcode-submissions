def add_two_numbers() -> int:
    user_input = input()
    values = user_input.split(",")

    return_val = int(values[0]) + int(values[1])
    return return_val


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())

from main_algorythm import count_roots


def input_number(variable_name, value):
    try:
        return float(value)
    except ValueError:
        print(f"Error. Expected a valid real number, got {value} instead")
        return input_number(variable_name, input(f'{variable_name} - '))


def solve_console_equation():
    a = input_number("a", input("a - "))
    b = input_number("b", input("b - "))
    c = input_number("c", input("c - "))
    return count_roots(a, b, c)

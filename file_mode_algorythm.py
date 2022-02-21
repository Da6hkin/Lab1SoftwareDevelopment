from main_algorythm import count_roots


def solve_file_equation():
    file = open("numbers.txt", "r")
    line = file.readline()
    numbers_list = line.split(" ")
    if (len(numbers_list) != 3):
        return "The text file must contain 3 numbers separated by a space"
    else:
        try:
            a = float(numbers_list[0])
            b = float(numbers_list[1])
            c = float(numbers_list[2])
            return count_roots(a, b, c)
        except VaultError:
            return f"Error. Expected a valid real number, got {value} instead"

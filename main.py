from console_algorythm import solve_console_equation
from file_mode_algorythm import solve_file_equation


def main():
    print("Select solution mode \nInteractive = 1 \nNon-Interactive = 2")
    mode = input("Type 1 or 2: ")
    try:
        if int(mode) == 1:
            return solve_console_equation()
        elif int(mode) == 2:
            return solve_file_equation()
        else:
            print("Only 1 or 2 available")
            return main()
    except ValueError:
        print("Only 1 or 2 available")
        return main()


if __name__ == "__main__":
    main()

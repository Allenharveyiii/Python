import random
import output

"""Returns the users choice

Handles the main menu.
Makes sure the user entered a valid input.
"""


def main_display():
    is_valid = False
    display_choice = -1
    while not is_valid:
        print("Please select an option.\n")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Division")
        print("4. Multiplication")

        display_choice = input()
        if int(display_choice) in range(1, 5):
            is_valid = True
        else:
            print("Please enter a valid option")
    return display_choice


"""No Return

Handles the conditional statements for each choice.
"""


def problem_choice(choice, num_of_problems, lower_range, upper_range, filename):
    if choice is "1":
        problems = create_problems("+", num_of_problems, lower_range, upper_range)
        output.problems_to_txt(problems, filename, "+")
    elif choice is "2":
        problems = create_problems("-", num_of_problems, lower_range, upper_range)
        output.problems_to_txt(problems, filename, "-")
    elif choice is "3":
        problems = create_problems("/", num_of_problems, lower_range, upper_range)
        output.problems_to_txt(problems, filename, "/")
    else:
        problems = create_problems("*", num_of_problems, lower_range, upper_range)
        output.problems_to_txt(problems, filename, "*")


"""Returns the lower and upper range of the numbers to be in the problems

With the difficulty setting from the user, this method gets the range
of numbers to be used in the problems.
"""


def get_range(diff):
    if diff is "1":
        low_range = 0
        up_range = 10
    elif diff is "2":
        low_range = 10
        up_range = 25
    elif diff is "3":
        low_range = 25
        up_range = 50
    elif diff is "4":
        low_range = 10
        up_range = 100
    elif diff is "5":
        low_range = 100
        up_range = 1000
    else:
        low_range = 10
        up_range = 25
    return low_range, up_range


"""Returns a list of problems

Creates the problems with the specifications entered by the user.
"""


def create_problems(operator, number_of_problems, low_range, up_range):
    problem_list = []
    for count in range(0, int(number_of_problems)):
        num1 = random.randrange(int(low_range), int(up_range))
        num2 = random.randrange(int(low_range), int(up_range))
        problem_list.append(output.problem_format(num1, num2, operator))
    return problem_list


result = main_display()
number_of_problems_main = input("How many problems would you like to generate?")
difficulty = input("What level of difficulty would you like? (1-5)")
filename = input("What do you want the name of the file to be?")
low_range_main, up_range_main = get_range(difficulty)

problem_choice(result, number_of_problems_main, low_range_main, up_range_main, filename)



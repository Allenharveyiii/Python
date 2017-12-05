"""Returns a formatted problem

Used to give the problems a consistent format for cleaner output.
"""


def problem_format(num1, num2, operator):
    problem = '''%7s
%-3s %3s
--------
    ''' % (num1, operator, num2)
    return problem


"""No Return

Used to write the problems out to a file
"""


def problems_to_txt(problems, filename, operator):
    filename = filename + ".txt"
    file = open(filename, "w+")
    title = ""
    if operator is "+":
        title = "Addition Practice Problems"
    elif operator is "-":
        title = "Subtraction Practice Problems"
    elif operator is "/":
        title = "Division Practice Problems"
    elif operator is "*":
        title = "Multiplication Practice Problems"
    file.write(title+"\n\n")
    for problem in range(len(problems)):
        file.write(problems[problem]+"\n\n")
    file.close()
    print("%s was created." % filename)

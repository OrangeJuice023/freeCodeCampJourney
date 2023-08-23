def validate_problems(problems):
    if len(problems) > 5:
        return "Error: Too many problems."

    operators = {'+', '-', '*', '/'}
    for problem in problems:
        num1, operator, num2 = problem.split()

        if operator not in operators:
            return "Error: Operator must be '+', '-', '*', or '/'."

        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

    return None

def generate_lines(problems, show_answers=False):
    lines = []
    for problem in problems:
        num1, operator, num2 = problem.split()

        width = max(len(num1), len(num2)) + 2
        line1 = num1.rjust(width)
        line2 = operator + num2.rjust(width - 1)
        dashes = '-' * width

        lines.extend([line1, line2, dashes])

    if show_answers:
        solutions = [sol.rjust(len(line)) for line, _, sol in arranged_problems]
        lines.append('    '.join(solutions))

    return lines

def arithmetic_arranger(problems, val=False):
    validation_error = validate_problems(problems)
    if validation_error:
        return validation_error

    arranged_problems = generate_lines(problems, val)

    return '\n'.join(arranged_problems)

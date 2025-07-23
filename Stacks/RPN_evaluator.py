# Understood RPN Evaluator Problem and Solution
def RPN_evaluator(expression):
    expression = expression.split(", ")
    intermediate_results = []
    OPERATORS = {"+": lambda y, x: int(x) + int(y), "-": lambda y, x: int(x) - int(y), "*": lambda y, x: int(x) * int(y), "/": lambda y, x: int(int(x) / int(y))}
    for exp_ in expression:
        if exp_ in OPERATORS:
            y = intermediate_results.pop()
            x = intermediate_results.pop()
            intermediate_results.append(OPERATORS[exp_](y, x))
        else:
            intermediate_results.append(exp_)
    return intermediate_results[-1]


print(RPN_evaluator("3, 4, +"))
def calc(expression: str) -> float:
    def parse_expression():
        term = parse_term()

        while len(tokens) > 0 and (tokens[0] == "+" or tokens[0] == "-"):
            operator = tokens.pop(0)
            rhs = parse_term()
            if operator == "+":
                term += rhs
            else:
                term -= rhs

        return term

    def parse_term():
        factor = parse_factor()

        while len(tokens) > 0 and (tokens[0] == "*" or tokens[0] == "/"):
            operator = tokens.pop(0)
            rhs = parse_factor()
            if operator == "*":
                factor *= rhs
            else:
                factor /= rhs

        return factor

    def parse_factor():
        if len(tokens) > 0 and tokens[0] == "-":
            tokens.pop(0)
            factor = -parse_factor()
        elif len(tokens) > 0 and tokens[0] == "(":
            tokens.pop(0)
            factor = parse_expression()
            if len(tokens) == 0 or tokens.pop(0) != ")":
                raise ValueError("Mismatched parentheses")
        elif len(tokens) > 0 and tokens[0].isdigit():
            factor = float(tokens.pop(0))

        return factor

    tokens = []
    i = 0

    while i < len(expression):
        if expression[i].isdigit() or expression[i] == ".":
            j = i
            while j < len(expression) and \
            (expression[j].isdigit() or expression[j] == "."):
                j += 1
            tokens.append(expression[i:j])
            i = j
        elif expression[i] in "+-*/()":
            tokens.append(expression[i])
            i += 1
        else:
            i += 1

    result = parse_expression()

    return result

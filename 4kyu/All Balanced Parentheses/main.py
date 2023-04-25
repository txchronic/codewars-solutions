def balanced_parens(n: int) -> list:
    def generator(open_count: int, close_count: int) -> str:
        if open_count == close_count == 0:
            yield ""
        else:
            if open_count > 0:
                for j in generator(open_count - 1, close_count):
                    yield "(" + j

            if close_count > open_count:
                for j in generator(open_count, close_count - 1):
                    yield ")" + j

    return list(generator(n, n))

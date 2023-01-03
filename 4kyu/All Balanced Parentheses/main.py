def balanced_parens(n: int) -> list:
    def generator(count: int, step = None) -> str:
        step = count if step is None else step

        if count == step == 0:
            yield ""
        else:
            if count > 0:
                for j in generator(count - 1, step):
                    yield "(" + j

            if step > count:
                for j in generator(count, step - 1):
                    yield ")" + j
    
    return list(generator(n))
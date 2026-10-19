def compose(f, g):
    def fn(x):
        return f(g(x))
    return fn

def pipe(* funcs):
    def pipeline(value):
        result = value
        for func in funcs:
            result = func(result)
        return result
    return pipeline

add_one = lambda x: x + 1
double = lambda x: x * 2

print(compose(add_one, double)(5))
print(pipe(add_one, double)(5))

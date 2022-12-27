
def line_by_ine(*args):
    for n in args:
        print(n)  # 一 个 一


def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(1, 2, 10, 14))


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(kwargs)
    return n


print(calculate(10, multiply=2, add=2))


class Motorcycle:
    def __init__(self,**kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.kwarg = kw


Honda_Rebel = Motorcycle(make="Honda", model="2021 300")

print(Honda_Rebel.make, Honda_Rebel.model, Honda_Rebel.kwarg)



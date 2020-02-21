##Usually in languages like C, C++, Java only one value can be returned from a
##function
##But in a Python function multiple values can be returned

def calculator(a, b):
    add = a + b
    sub = a - b
    mult = a * b
    div = float(a) / float(b)

    print(add, sub, mult, div)

    return add, sub, mult, div

answers = calculator(10, 3)
print(answers)
#answers is a tuple

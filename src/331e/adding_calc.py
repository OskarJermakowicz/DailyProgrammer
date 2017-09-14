def add(a, b):
    return a + b

def sub(a, b):
    res = 0
    if b < a:
        incr = 1
    else:
        incr = -1
        a, b = b, a
    while b < a:
        res += incr
        b += 1
    return res

def mul(a, b):
    res = 0
    if a < 0 and b < 0:
        res = sum([res + abs(b) for i in range(0, abs(a))])
    elif a < 0:
        res = sum([res + a for i in range(0,b)])
    else:
        res = sum([res + b for i in range(0,a)])
    return res

def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    if a < 0 and b < 0:
        a = sub(0, a)
        b = sub(0, b)
    if a >= 0 and b >= 0:
        incr = 1
    elif a < 0:
        a = sub(0, a)
        incr = -1
    elif b < 0:
        b = sub(0, b)
        incr = -1
    res = 0
    old_t = 0
    t = b
    while a >= t:
        old_t = t
        t += b
        res += incr
    if old_t != a:
        raise ValueError
    return res

def exp(a, b):
    if b < 0:
        raise ValueError
    res = 1
    for i in range(0,b):
        res = mul(res, a)
    return res

operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    '^': exp
}

inputs = ['12 + 25',
          '-30 + 100',
          '100 - 30',
          '100 - -30',
          '-25 - 29',
          '-41 - -10',
          '9 * 3',
          '9 * -4',
          '-4 * 8',
          '-12 * -9',
          '100 / 2',
          '75 / -3',
          '-75 / 3',
          '7 / 3',
          '0 / 0',
          '5 ^ 3',
          '-5 ^ 3',
          '-8 ^ 3',
          '-1 ^ 1',
          '1 ^ 1',
          '0 ^ 5',
          '5 ^ 0',
          '10 ^ -3']

for input in inputs:
    a, op, b = input.split()
    try:
        print(input, '=', operations[op](int(a), int(b)))
    except ValueError:
        print(input, '=', "Non-integral answer")
    except ZeroDivisionError:
        print(input, '=', "Not-defined")
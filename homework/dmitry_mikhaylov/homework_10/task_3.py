def calculate(func):
    def wrapper(*args):
        if args[0] == args[1]:
            operation = '+'
        elif args[0] < 0 or args[1] < 0:
            operation = '*'
        elif args[0] > args[1]:
            operation = '-'
        else:
            operation = '/'
        return func(args[0], args[1], operation)
    return wrapper


@calculate
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


print(calc(2, 3)) # /
print(calc(0, 1)) # /
print(calc(1, 0)) # -
print(calc(2, -3)) # *
print(calc(-2, 3)) # *
print(calc(-2, -3)) # *
print(calc(3, 2)) # -
print(calc(-2, -2)) # +
print(calc(2, 2)) # +

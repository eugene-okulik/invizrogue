def repeat_me(count):
    def actual_dec(func):
        def wrapper(*args):
            for times in range(count):
                func(*args)
        return wrapper
    return actual_dec


@repeat_me(count=2)
def example(text):
    print(text)


example('print me')

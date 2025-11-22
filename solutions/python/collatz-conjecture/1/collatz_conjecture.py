def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    step = 0
    while number != 1:
        remainder = number % 2
        if remainder == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        step += 1
    return step

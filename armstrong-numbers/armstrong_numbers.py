def is_armstrong_number(number):
    exponent = len(str(number))
    number_to_string = str(number)
    armstrong_op = map(lambda x: int(x)**exponent, number_to_string)
    return True if sum(armstrong_op) == number else False

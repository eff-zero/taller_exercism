EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


print(bake_time_remaining.__doc__)


def preparation_time_in_minutes(numbers_of_layers):
    """DOCUMENTATION"""
    return PREPARATION_TIME * numbers_of_layers


print(preparation_time_in_minutes.__doc__)


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """DOCUMENTATION"""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


print(elapsed_time_in_minutes.__doc__)

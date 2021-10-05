def equilateral(sides):
    sides.sort()
    two_sides_sum = sides[0] + sides[1]
    third_side = sides[2]
    if 0 in sides or two_sides_sum <= third_side:
        return False
    count_side = sides.count(third_side)
    if count_side == 3:
        return True
    return False


def isosceles(sides):
    sides.sort()
    two_sides_sum = sides[0] + sides[1]
    third_side = sides[2]
    if 0 in sides or two_sides_sum <= third_side:
        return False
    count_side = sides.count(third_side)
    if count_side == 2 or count_side == 3:
        return True
    return False


def scalene(sides):
    sides.sort()
    two_sides_sum = sides[0] + sides[1]
    third_side = sides[2]
    if 0 in sides or two_sides_sum <= third_side:
        return False
    count_side = sides.count(third_side)
    if count_side == 1:
        return True
    return False

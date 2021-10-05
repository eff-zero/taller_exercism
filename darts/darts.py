def score(x, y):
    # (x-h)² + (y-k)² = r² , circle ecuation
    # h,k(0,0) -> (x)² + (y)² = r² [real ecuation]
    ecuation = (x)**2 + (y)**2
    r_2 = {'outer_circle': 100,
           'middle_circle': 25,
           'inner_circle': 1}
    if ecuation <= r_2['outer_circle'] and ecuation > r_2['middle_circle']:
        return 1
    if ecuation <= r_2['middle_circle'] and ecuation > r_2['inner_circle']:
        return 5
    if ecuation <= r_2['inner_circle']:
        return 10
    return 0

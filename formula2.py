def starSortSimple(ns):
    v = sum(ns) # number of votes
    m = 3 # minimum votes the be exposed on the list
    C = 4.5867 # the mean vote across the whole report
    # R: average ratings
    R = ((5 * ns[0]) + (4.5 * ns[1]) + (4 * ns[2]) + (3.5 * ns[3]) + (3 * ns[4]) + (2.5 * ns[5]) + (2 * ns[6]) + (1.5 * ns[7]) + (1 * ns[8]) + (0.5 * ns[9]) + 0) / v
    return ((v / (v + m)) * R) + (( m / ( v + m )) * C)
    # return (v * R + m * C) / (v + m) it's the same

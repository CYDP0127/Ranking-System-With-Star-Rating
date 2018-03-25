import math
def starSortLog(ns) :
    v = sum(ns)
    R = ((5 * ns[0]) + (4.5 * ns[1]) + (4 * ns[2]) + (3.5 * ns[3]) + (3 * ns[4]) + (2.5 * ns[5]) + (2 * ns[6]) + (1.5 * ns[7]) + (1 * ns[8]) + (0.5 * ns[9]) + 0) / v
    return math.log(v) * R

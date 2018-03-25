import math
def starSortLog(ns) :
    v = sum(ns)
    R = ((5 * ns[0]) + (4.5 * ns[1]) + (4 * ns[2]) + (3.5 * ns[3]) + (3 * ns[4]) + (2.5 * ns[5]) + (2 * ns[6]) + (1.5 * ns[7]) + (1 * ns[8]) + (0.5 * ns[9]) + 0) / v
    return math.log(v) * R

print(starSortLog((	1	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	)))
print(starSortLog((	0	,	5	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	)))
print(starSortLog((	0	,	0	,	10	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	)))
print(starSortLog((	0	,	0	,	0	,	20	,	0	,	0	,	0	,	0	,	0	,	0	,	0	)))
print(starSortLog((	0	,	0	,	0	,	0	,	30	,	0	,	0	,	0	,	0	,	0	,	0	)))
print(starSortLog((	0	,	0	,	0	,	0	,	0	,	40	,	0	,	0	,	0	,	0	,	0	)))
print(starSortLog((	0	,	0	,	0	,	0	,	0	,	0	,	50	,	0	,	0	,	0	,	0	)))
print(starSortLog((	0	,	0	,	0	,	0	,	0	,	0	,	0	,	60	,	0	,	0	,	0	)))
print(starSortLog((	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	70	,	0	,	0	)))
print(starSortLog((	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	80	,	0	)))
print(starSortLog((	100	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	)))
print(starSortLog((	60	,	20	,	10	,	5	,	3	,	1	,	1	,	0	,	0	,	0	,	0	)))
print(starSortLog((	50	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	50	,	0	)))
print(starSortLog((	30	,	15	,	5	,	0	,	0	,	0	,	0	,	5	,	15	,	30	,	0	)))
print(starSortLog((	10	,	10	,	10	,	10	,	10	,	10	,	10	,	10	,	10	,	10	,	10	)))

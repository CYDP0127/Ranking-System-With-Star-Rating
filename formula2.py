def starSortSimple(ns):
    v = sum(ns)
    m = 3 # minimum vote
    C = 4.5867
    R = ((5 * ns[0]) + (4.5 * ns[1]) + (4 * ns[2]) + (3.5 * ns[3]) + (3 * ns[4]) + (2.5 * ns[5]) + (2 * ns[6]) + (1.5 * ns[7]) + (1 * ns[8]) + (0.5 * ns[9]) + 0) / v
    return ((v / (v + m)) * R) + (( m / ( v + m )) * C)
    # return (v * R + m * C) / (v + m)
print(starSortSimple((	1	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	)))
print(starSortSimple((	0	,	5	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	)))
print(starSortSimple((	0	,	0	,	10	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	)))
print(starSortSimple((	0	,	0	,	0	,	20	,	0	,	0	,	0	,	0	,	0	,	0	,	0	)))
print(starSortSimple((	0	,	0	,	0	,	0	,	30	,	0	,	0	,	0	,	0	,	0	,	0	)))
print(starSortSimple((	0	,	0	,	0	,	0	,	0	,	40	,	0	,	0	,	0	,	0	,	0	)))
print(starSortSimple((	0	,	0	,	0	,	0	,	0	,	0	,	50	,	0	,	0	,	0	,	0	)))
print(starSortSimple((	0	,	0	,	0	,	0	,	0	,	0	,	0	,	60	,	0	,	0	,	0	)))
print(starSortSimple((	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	70	,	0	,	0	)))
print(starSortSimple((	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	80	,	0	)))
print(starSortSimple((	100	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	)))
print(starSortSimple((	60	,	20	,	10	,	5	,	3	,	1	,	1	,	0	,	0	,	0	,	0	)))
print(starSortSimple((	50	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	50	,	0	)))
print(starSortSimple((	30	,	15	,	5	,	0	,	0	,	0	,	0	,	5	,	15	,	30	,	0	)))
print(starSortSimple((	10	,	10	,	10	,	10	,	10	,	10	,	10	,	10	,	10	,	10	,	10	)))

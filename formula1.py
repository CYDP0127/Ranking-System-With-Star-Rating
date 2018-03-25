import math
def starsort(ns):
    """
    http://www.evanmiller.org/ranking-items-with-star-ratings.html
    https://stackoverflow.com/questions/1411199/what-is-a-better-way-to-sort-by-a-5-star-rating
    """
    N = sum(ns)
    K = len(ns)
    s = list(range(K,0,-1))
    s2 = [sk**2 for sk in s]
    z = 1.65
    def f(s, ns):
        N = sum(ns)
        K = len(ns)
        return sum(sk*(nk+1) for sk, nk in zip(s,ns)) / (N+K)
    fsns = f(s, ns)
    return fsns - z*math.sqrt((f(s2, ns)- fsns**2)/(N+K+1))

print(starsort((1,0,0,0,0,0,0,0,0,0)))

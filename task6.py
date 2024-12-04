def F(n):
    N = 1
    if n > 1:
        N = F(n-1) + pow(2, n-1)
    return N


print(F(12))

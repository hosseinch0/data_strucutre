def choose(n=4, k=3):
    if k == 0:
        return 1
    elif n < k:
        return 0
    else:
        return choose(n-1, k-1) + choose(n-1, k)

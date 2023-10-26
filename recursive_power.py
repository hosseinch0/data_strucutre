def recursive_power(base=2, power=3):
    if power == 0:
        return 1
    else:
        return base * recursive_power(base, power - 1)

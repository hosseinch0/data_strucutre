base = int(input("Insert the base: "))
power = int(input("Insert the power: "))


def recursive_power(base, power):
    if power == 0:
        return 1
    else:
        return base * recursive_power(base, power - 1)


print(recursive_power(base, power))

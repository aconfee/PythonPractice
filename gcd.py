def gcd(a, b):
    if b == 0:
        return a

    return abs(gcd(b, a % b))

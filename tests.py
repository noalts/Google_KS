a, n = [int(input()) for _ in range(2)]

def power(s, t):
    if t == 0:
        return 1
    s = s * power(s, t - 1)
    return s

print(power(a, n))
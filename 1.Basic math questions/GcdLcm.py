def GcdLcm(n1, n2):
    gcd = 1
    k = min(n1, n2)
    for i in range(1, k + 1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i

    lcm = (n1 * n2) // gcd

    return gcd, lcm


print(GcdLcm(14, 8))

# Optimal


def GcdLcm(n1, n2):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    Gcd = gcd(n1, n2)  # nested function

    Lcm = (n1 * n2) // Gcd

    return Lcm, Gcd


lcm, gcd = GcdLcm(14, 8)
print(f"Lcm={lcm}, Gcd={gcd}")

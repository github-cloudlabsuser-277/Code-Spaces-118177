def prime(n):   # n is a positive integer
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True



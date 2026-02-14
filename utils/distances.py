import math

def minkowski(a, b, p):
    # Genel Minkowski mesafe formülü: (|a1-b1|^p + |a2-b2|^p + ...)^(1/p)
    return sum(abs(x - y) ** p for x, y in zip(a, b)) ** (1 / p)

def manhattan(a, b):
    # Minkowski'nin p=1 özel halidir
    return minkowski(a, b, 1)

def euclidean(a, b):
    # Minkowski'nin p=2 özel halidir (Pisagor teoremi gibi)
    return minkowski(a, b, 2)

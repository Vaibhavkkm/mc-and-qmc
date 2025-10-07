import math
import random

n = int(input("N: "))
points_in = 0

for _ in range(n):
    t = (random.random(), random.random())
    if math.sqrt(t[0]**2 + t[1]**2) <= 1:
        points_in += 1

print(f"π ≈ {4 * (points_in / n)}")
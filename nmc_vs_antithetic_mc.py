import math
import random
import time

n = int(input("N: "))

# Normal Monte Carlo(NMC)
start_normal = time.time()
points_in_normal = 0
for _ in range(n):
    t = (random.random(), random.random())
    if math.sqrt(t[0]**2 + t[1]**2) <= 1:
        points_in_normal += 1
end_normal = time.time()
pi_normal = 4 * (points_in_normal / n)
time_normal = end_normal - start_normal
print(f"Normal MC: π ≈ {pi_normal}, Time: {time_normal:.4f} seconds")

# Antithetic Variates
start_anti = time.time()
points_in_anti = 0
for _ in range(n // 2):
    x = random.random()
    y = random.random()
    if math.sqrt(x**2 + y**2) <= 1:
        points_in_anti += 1
    x2 = 1 - x
    y2 = 1 - y
    if math.sqrt(x2**2 + y2**2) <= 1:
        points_in_anti += 1
if n % 2 == 1:
    x = random.random()
    y = random.random()
    if math.sqrt(x**2 + y**2) <= 1:
        points_in_anti += 1
end_anti = time.time()
pi_anti = 4 * (points_in_anti / n)
time_anti = end_anti - start_anti
print(f"Antithetic Variates: π ≈ {pi_anti}, Time: {time_anti:.4f} seconds")
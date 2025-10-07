import math
import random
import time

def halton_sequence(index, base):
    # Generate single coordinate for Halton sequence..
    result = 0.0
    f = 1.0 / base
    i = index
    while i > 0:
        result += f * (i % base)
        i = math.floor(i / base)
        f /= base
    return result

def generate_halton_point(i):
    # generate 2D Halton point using bases 2 and 3.
    x = halton_sequence(i + 1, 2)  # i+1 to avoid (0,0) -> Sqrt of 0+0 = 0 ( We dont wanna avoid the first point to come in centre of the circle and wasting evennesss)
    y = halton_sequence(i + 1, 3)
    return x, y

n = int(input("N: "))

# Standard Monte Carlo (MC)
start_mc = time.time()
points_in_mc = 0
for _ in range(n):
    t = (random.random(), random.random())
    if math.sqrt(t[0]**2 + t[1]**2) <= 1:
        points_in_mc += 1
pi_mc = 4 * (points_in_mc / n)
time_mc = time.time() - start_mc

# Quasi Monte Carlo(QMC) with Halton 
start_qmc = time.time()
points_in_qmc = 0
for i in range(n):
    t = generate_halton_point(i)
    if math.sqrt(t[0]**2 + t[1]**2) <= 1:
        points_in_qmc += 1
pi_qmc = 4 * (points_in_qmc / n)
time_qmc = time.time() - start_qmc

print(f"MC π ≈ {pi_mc} (time: {time_mc:.4f}s)")
print(f"QMC π ≈ {pi_qmc} (time: {time_qmc:.4f}s)")
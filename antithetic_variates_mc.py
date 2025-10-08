import math
import random
import time

n = int(input("N: "))
start = time.time()
points_in = 0

for _ in range(n // 2):
    x = random.random()
    y = random.random()
    if math.sqrt(x**2 + y**2) <= 1:
        points_in += 1
    x2 = 1 - x
    y2 = 1 - y
    if math.sqrt(x2**2 + y2**2) <= 1:
        points_in += 1

if n % 2 == 1:
    x = random.random()
    y = random.random()
    if math.sqrt(x**2 + y**2) <= 1:
        points_in += 1

end = time.time()
pi_est = 4 * (points_in / n)
print(f"π ≈ {pi_est}")
print(f"Time taken: {end - start} seconds")
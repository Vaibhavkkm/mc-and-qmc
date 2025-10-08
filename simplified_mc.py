import math
import random
import time

n = int(input("N: "))
start = time.time()
points_in = 0

for _ in range(n):
    t = (random.random(), random.random())
    if math.sqrt(t[0]**2 + t[1]**2) <= 1:
        points_in += 1

end = time.time()
pi_est = 4 * (points_in / n)
print(f"π ≈ {pi_est}")
print(f"Time taken: {end - start} seconds")
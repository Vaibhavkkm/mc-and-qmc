import random
import time

n = int(input("N: "))

# Normal Monte Carlo
start_normal = time.time()
points_in_normal = 0
for _ in range(n):
    x = random.random()
    y = random.random()
    if x**2 + y**2 <= 1:
        points_in_normal += 1
end_normal = time.time()
pi_normal = 4 * (points_in_normal / n)
time_normal = end_normal - start_normal
print(f"Normal MC: π ≈ {pi_normal}, Time: {time_normal:.4f} seconds")

# Stratified Sampling
K = 4  # number of strata
start_strat = time.time()
points_in_strat = 0
samples_per_stratum = n // K
extra = n % K
for j in range(K):
    low = j / K
    high = (j + 1) / K
    num_samples = samples_per_stratum + 1 if j < extra else samples_per_stratum
    for _ in range(num_samples):
        x = random.uniform(low, high)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            points_in_strat += 1
end_strat = time.time()
pi_strat = 4 * (points_in_strat / n)
time_strat = end_strat - start_strat
print(f"Stratified: π ≈ {pi_strat}, Time: {time_strat:.4f} seconds")
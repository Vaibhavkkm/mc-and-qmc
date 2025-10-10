import math
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

# Control Variate
start_cv = time.time()
points_in_cv = 0
I_list = []
g_list = []
for _ in range(n):
    x = random.random()
    y = random.random()
    r2 = x**2 + y**2
    g = 1 - r2
    I = 1 if r2 <= 1 else 0
    points_in_cv += I
    I_list.append(I)
    g_list.append(g)
mean_I = points_in_cv / n
mean_g = sum(g_list) / n
mu = 1 / 3.0
sum_cov = 0.0
sum_var_g = 0.0
for i in range(n):
    dI = I_list[i] - mean_I
    dg = g_list[i] - mean_g
    sum_cov += dI * dg
    sum_var_g += dg**2
cov = sum_cov / (n - 1) if n > 1 else 0
var_g = sum_var_g / (n - 1) if n > 1 else 0
c = -cov / var_g if var_g != 0 else 0
cv_adjust = c * (mean_g - mu)
pi_cv = 4 * (mean_I + cv_adjust)
end_cv = time.time()
time_cv = end_cv - start_cv
print(f"Control Variate: π ≈ {pi_cv}, Time: {time_cv:.4f} seconds")
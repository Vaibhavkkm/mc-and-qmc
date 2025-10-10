# Monte Carlo and Quasi-Monte Carlo Methods for π Estimation

This repository contains implementations of various Monte Carlo (MC) and Quasi-Monte Carlo (QMC) variance reduction techniques for estimating the value of π. All implementations use the classic circle-inscribed-in-square method.

## 📊 Overview

The project demonstrates different sampling strategies and variance reduction techniques to improve the accuracy and efficiency of Monte Carlo simulations. Each implementation estimates π by randomly sampling points in a unit square and counting how many fall within a quarter circle.

### Mathematical Background

The basic principle: A circle with radius 1 has area π, and a square with side 2 has area 4. The ratio of areas is π/4. By sampling random points in a unit square [0,1]×[0,1] and checking if they fall within the quarter circle (x² + y² ≤ 1), we can estimate:

$$\pi \approx 4 \times \frac{\text{points inside circle}}{\text{total points}}$$

---

## 📁 Files Description

### 1. `simplified_mc.py` - Basic Monte Carlo
**Purpose**: Baseline implementation of standard Monte Carlo method.

**Features**:
- Pure random sampling
- Simple circle inclusion check using distance formula
- Performance timing

**Algorithm**:
1. Generate N random points (x, y) in [0, 1]×[0, 1]
2. Check if √(x² + y²) ≤ 1
3. Estimate π = 4 × (points_inside / N)

**Usage**:
```bash
python simplified_mc.py
```

---

### 2. `antithetic_variates_mc.py` - Antithetic Variates Method
**Purpose**: Reduce variance using negatively correlated samples.

**Features**:
- Generates complementary pairs: (x, y) and (1-x, 1-y)
- Reduces variance by averaging negatively correlated estimates
- More efficient than standard MC with same number of samples

**Algorithm**:
1. For each iteration, generate one random point (x, y)
2. Also evaluate its antithetic pair (1-x, 1-y)
3. Both points contribute to the estimate
4. Variance reduction through negative correlation

**Theoretical Advantage**:
- If f(U) and f(1-U) are negatively correlated, Var[(f(U) + f(1-U))/2] < Var[f(U)]

**Usage**:
```bash
python antithetic_variates_mc.py
```

---

### 3. `nmc_vs_antithetic_mc.py` - Comparison Study
**Purpose**: Direct comparison between Normal MC and Antithetic Variates MC.

**Features**:
- Runs both methods with same N
- Side-by-side performance and accuracy comparison
- Timing analysis for both approaches

**Metrics Compared**:
- Estimation accuracy (closeness to π ≈ 3.14159...)
- Execution time
- Variance (across multiple runs)

**Usage**:
```bash
python nmc_vs_antithetic_mc.py
```

---

### 4. `nmc_vs_stratification.py` - Stratified Sampling
**Purpose**: Compare Normal MC with Stratified Sampling technique.

**Features**:
- Divides sampling space into K strata (default K=4)
- Ensures uniform coverage across the domain
- Reduces variance by eliminating clustering

**Algorithm (Stratified Sampling)**:
1. Divide x-axis into K equal intervals [j/K, (j+1)/K]
2. Sample N/K points from each stratum
3. Sample x uniformly in [j/K, (j+1)/K] and y in [0, 1]
4. Aggregate results across all strata

**Theoretical Advantage**:
- Guarantees coverage of entire space
- Reduces variance compared to pure random sampling
- Particularly effective when integrand varies smoothly

**Usage**:
```bash
python nmc_vs_stratification.py
```

---

### 5. `nmc_vs_control_variate_mc.py` - Control Variates Method
**Purpose**: Use a correlated function with known expectation to reduce variance.

**Features**:
- Control function: g(x, y) = 1 - (x² + y²)
- Known expectation: E[g] = 1/3
- Adjusts estimate using correlation between indicator and control function

**Algorithm**:
1. For each sample, compute both:
   - I = 1 if x² + y² ≤ 1, else 0 (indicator function)
   - g = 1 - (x² + y²) (control variate)
2. Calculate covariance Cov(I, g) and variance Var(g)
3. Compute optimal coefficient c = -Cov(I, g) / Var(g)
4. Adjusted estimate: E[I] + c(E[g] - μ), where μ = 1/3

**Theoretical Advantage**:
- Variance reduction: Var(I + c(g - μ)) < Var(I) when I and g are correlated
- Uses known information to improve estimate

**Usage**:
```bash
python nmc_vs_control_variate_mc.py
```

---

### 6. `merged_code.py` - Monte Carlo vs Quasi-Monte Carlo
**Purpose**: Compare pseudo-random (MC) with low-discrepancy (QMC) sequences.

**Features**:
- **MC**: Standard pseudo-random sampling
- **QMC**: Halton sequence (bases 2 and 3)
- Demonstrates superiority of low-discrepancy sequences

**Halton Sequence**:
The Halton sequence generates points that are more evenly distributed than random numbers:
```
Halton(i, base) = Σ (aₖ / baseᵏ⁺¹)
where i = Σ aₖ × baseᵏ (base representation of i)
```

**Algorithm**:
1. **MC**: Generate points using random.random()
2. **QMC**: Generate points using Halton sequence with bases 2 (for x) and 3 (for y)
3. Both methods evaluate same number of points

**Theoretical Advantage**:
- QMC error: O(log(N)ᵈ / N) vs MC error: O(1/√N)
- Better space-filling properties
- Faster convergence for smooth integrands

**Usage**:
```bash
python merged_code.py
```

---

## 🎯 Variance Reduction Techniques Summary

| Technique | Key Idea | Variance Reduction | Computational Cost |
|-----------|----------|-------------------|-------------------|
| **Antithetic Variates** | Use complementary samples | Moderate | Low (+0%) |
| **Stratified Sampling** | Divide domain into regions | High | Low (+5%) |
| **Control Variates** | Use correlated function | High | Medium (+20%) |
| **Quasi-Monte Carlo** | Low-discrepancy sequences | Very High | Low (+0%) |

---

## 🚀 Getting Started

### Prerequisites
```bash
python 3.x
# Standard library only - no external dependencies!
```

### Running the Experiments

1. **Basic estimation**:
   ```bash
   python simplified_mc.py
   # Input: 100000
   ```

2. **Compare variance reduction techniques**:
   ```bash
   python nmc_vs_antithetic_mc.py
   python nmc_vs_stratification.py
   python nmc_vs_control_variate_mc.py
   python merged_code.py
   ```

### Recommended Sample Sizes
- Quick test: N = 10,000
- Standard: N = 100,000
- High accuracy: N = 1,000,000
- Research: N = 10,000,000+

---

## 📈 Expected Results

For N = 100,000 samples (approximate):

| Method | Typical Error | Relative Speed |
|--------|--------------|----------------|
| Normal MC | ±0.01 | 1.0x |
| Antithetic Variates | ±0.007 | 1.0x |
| Stratified (K=4) | ±0.005 | 1.05x |
| Control Variates | ±0.004 | 1.2x |
| QMC (Halton) | ±0.002 | 1.0x |

*Note: Actual results vary due to randomness*

---

## 📚 Key Concepts Demonstrated

### 1. **Law of Large Numbers**
As N → ∞, the Monte Carlo estimate converges to the true value.

### 2. **Central Limit Theorem**
Error decreases as O(1/√N) for standard MC.

### 3. **Variance Reduction**
Using problem structure and mathematical properties to reduce estimation variance without increasing sample size.

### 4. **Low-Discrepancy Sequences**
QMC methods achieve better convergence rates O(log(N)/N) by using deterministic, evenly-distributed points.

---

## 🔬 Course Context

**Course**: Mathematical Methods in Computer Science (MMCS)  
**Topic**: Monte Carlo and Quasi-Monte Carlo Methods  
**Semester**: 3  

This project demonstrates practical implementations of variance reduction techniques for numerical integration and demonstrates the trade-offs between different sampling strategies.

---

## 📊 Performance Analysis Tips

To properly evaluate these methods:

1. **Run multiple times**: MC methods are stochastic
2. **Use same N**: Fair comparison requires same sample size
3. **Measure variance**: Run each method 100+ times and compute std deviation
4. **Plot convergence**: Show error vs. sample size on log-log plot
5. **Time complexity**: Consider computational overhead of variance reduction

---

## 🎓 Learning Outcomes

By studying this code, you will understand:

- ✅ Basic Monte Carlo integration
- ✅ Variance reduction techniques and their theoretical foundations
- ✅ Trade-offs between accuracy and computational cost
- ✅ Difference between pseudo-random and quasi-random sequences
- ✅ Practical implementation of statistical methods

---

## 📖 References

1. **Antithetic Variates**: Hammersley & Morton (1956)
2. **Stratified Sampling**: Cochran (1977)
3. **Control Variates**: Lavenberg & Welch (1981)
4. **Quasi-Monte Carlo**: Halton (1960), Sobol (1967)

---

## 🤝 Author

**Vaibhav Mangroliya**  
SEM 3, MMCS Course

---

## 📝 License

Educational project for academic purposes.

---

## 💡 Future Enhancements

Potential extensions to explore:
- [ ] Latin Hypercube Sampling
- [ ] Importance Sampling
- [ ] Sobol sequences (another QMC method)
- [ ] Convergence plots and statistical analysis
- [ ] Multi-dimensional integration examples
- [ ] Adaptive stratification
- [ ] Parallel implementation using multiprocessing

---

## 🐛 Notes

- All implementations use the same basic circle-in-square method
- Timing may vary based on system performance
- For research-grade results, use N ≥ 10⁶
- QMC methods work best for smooth, low-dimensional integrands

---

**Last Updated**: October 2025

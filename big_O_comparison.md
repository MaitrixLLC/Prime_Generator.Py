## Big-O comparison of three prime-generation approaches

This section compares the asymptotic running time (Big-O) of:

1. **Original RNS-based “digit counter” filter** (your first Python version)
2. **Improved RNS-based filter** (defer digit activation until `p²`)
3. **Sieve of Eratosthenes** (classic array sieve)

### Notation

- Let **N** be the maximum integer tested (inclusive).
- Let **π(x)** be the prime-counting function (number of primes ≤ x).
- Use the standard approximation:  
  `π(x) ~ x / ln(x)` for large `x`.
- We ignore constant factors and focus on asymptotic order.

---

## 1) Original RNS-based method (v1)

### Per-candidate cost
At candidate `n`, the code maintains digits for **all primes found so far**,
which is on the order of `π(n)` digits.

- Increment digits: `O(π(n))`
- Wrap digits: `O(π(n))`
- Check any zero digit: `O(π(n))`

So the work per candidate is:

- **T(n) = O(π(n))**

### Total cost up to N
\[
T(N) = \sum_{n=2}^{N} O(\pi(n))
\]

Using `π(n) ~ n / ln(n)`:

\[
T(N) \approx \int_2^N \frac{x}{\ln x} \, dx
      = \Theta\!\left(\frac{N^2}{\ln N}\right)
\]

**Result (v1):**
- **Time:** `Θ(N² / ln N)`  
- **Space:** `Θ(π(N))` digits stored (plus the prime list), i.e. about `Θ(N / ln N)`

**Intuition:** you do “trial division-like” work against *all* primes found so far,
even though most are larger than `sqrt(n)` and can’t divide `n`.

---

## 2) Improved RNS-based method (v2: activate digits at p²)

### Key change
Only “activate” prime `p` as a tracked modulus once the candidate reaches `p²`.
Therefore at candidate `n`, the active digits correspond roughly to primes `p ≤ sqrt(n)`:

- active digit count ≈ `π(√n)`

### Per-candidate cost
- **T(n) = O(π(√n))**

Using `π(√n) ~ √n / ln(√n) ≈ (2√n) / ln(n)`.

### Total cost up to N
\[
T(N) = \sum_{n=2}^{N} O(\pi(\sqrt{n}))
\]

Approximate with an integral:

\[
T(N) \approx \int_2^N \frac{\sqrt{x}}{\ln x} \, dx
      = \Theta\!\left(\frac{N^{3/2}}{\ln N}\right)
\]

**Result (v2):**
- **Time:** `Θ(N^(3/2) / ln N)`  
- **Space:** `Θ(π(√N))` active digits (plus storage for primes), i.e. about `Θ(√N / ln N)`

**Intuition:** you restored the classic “only test primes up to √n” behavior, but
implemented using running residues instead of division/mod.

---

## 3) Sieve of Eratosthenes (classic)

### Cost to generate all primes ≤ N
The sieve maintains a boolean array of length `N` and crosses off multiples.
Its well-known time complexity is:

- **Time:** `O(N log log N)`
- **Space:** `O(N)` (or `O(N)` bits with bit-packing; segmented versions reduce peak memory)

**Result (Eratosthenes):**
- **Time:** `O(N log log N)`
- **Space:** `O(N)`

**Intuition:** instead of testing each candidate against many primes, it marks
composites in bulk by stepping through arithmetic progressions.

---

## Summary table

| Algorithm | What it does | Time (to process all candidates ≤ N) | Space |
|---|---|---:|---:|
| Original RNS filter (v1) | Updates/checks residue digits for all primes found so far | `Θ(N² / ln N)` | `Θ(π(N))` |
| Improved RNS filter (v2) | Updates/checks only primes activated at `p²` (≈ primes ≤ √n) | `Θ(N^(3/2) / ln N)` | `Θ(π(√N))` active |
| Eratosthenes sieve | Marks composite multiples in an array | `O(N log log N)` | `O(N)` |

---

## Practical takeaway

- The improved RNS method **does improve the Big-O order** versus the original
  (from ~`N²`-like to ~`N^(3/2)`-like, ignoring logs).
- However, a true sieve such as **Eratosthenes** is still in a much faster
  asymptotic class (`N log log N`) for generating all primes up to a bound `N`.

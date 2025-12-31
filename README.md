# Prime_Generator.Py
Prime Number Generator Sieve doesn't use any division !

This short Python script uses very little processing power to generate primes starting with two.
It works by tracking a list of primes and a list of residues.
For each trial number being tested, a list of residues (digits) is checked for zero,
If zero is present in the "digits" array, then the trial number is not prime, otherwise, it is.
A list of primes forms the modulus for the list of residues.  This primes list continues to grow which advances
the range of trial numbers that can be tested.  The digits array is what we call a "residue number".
The "primes" array contains the modulus associated to each residue digit in the digits array.  
Have fun playing with this amazing little piece of code!

The python script only uses the "numpy" module, so it's simple to use and play with.

# Prime_Generator_ver2.py  (chatGPT improved version)
## Why this is much faster than your original

### Biggest win: defer digits until p²

In your original, once you found prime `p`, you immediately started updating
its digit for all subsequent candidates — even though for a long time it
cannot help (because any multiple of `p` below `p²` has a smaller factor that
would have already triggered a zero digit).

With the `p²` activation rule, the number of tracked digits stays around
`π(√n)` instead of `π(n)`.

For your “1000 primes” run, `n ≈ 7927`, so `√n ≈ 89`, and `π(89) = 24`. That
means you update/check ~24 digits per candidate instead of ~1000 digits.

### Second win: vectorized update + wrap + zero check

No Python loops per candidate. Your prior `wrap_digits + contains_zero` were
doing Python-level iteration, which dominates runtime.

### Third win: no `np.insert` in the hot loop

`np.insert` reallocates/copies arrays every time you add a prime. In this
rewrite, array growth happens only when a prime is activated (rare) and when
a prime is discovered (still not in the inner digit work).

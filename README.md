# Prime_Generator.Py
Prime Number Generator Sieve doesn't use any division !

This short Python script uses very little processing power to generate primes starting with two.
It works by tracking a list of primes and a list of residues.
For each trial number being tested, the list of residues is checked for zero,
If zero is present in the "digits" array, then the trial number is not prime, otherwise, it is.
The list of primes forms the modulus for the list of residues.  This list continues to grow which advnaces
the range of trial numbers that can be tested.  The digits arraay is what we call a "residue number".
Have fun playing with this amazing little piece of code!

The python script only uses the "numpy" module, so it's simple to use and play with.

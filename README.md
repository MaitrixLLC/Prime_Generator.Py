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

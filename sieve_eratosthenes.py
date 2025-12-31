#!/usr/bin/env python3
"""
Sieve of Eratosthenes

Examples:
  python sieve_eratosthenes.py 100          # primes <= 100
  python sieve_eratosthenes.py 100000 -c    # count primes <= 100000
  python sieve_eratosthenes.py 100000 -f primes.csv
"""

import argparse
import sys


def sieve_eratosthenes(n: int) -> list[int]:
    """Return a list of all primes <= n using the Sieve of Eratosthenes."""
    if n < 2:
        return []

    # bytearray is compact and fast for boolean flags
    is_prime = bytearray(b"\x01") * (n + 1)
    is_prime[0:2] = b"\x00\x00"  # 0 and 1 are not prime

    # Cross off multiples starting at p*p
    p = 2
    while p * p <= n:
        if is_prime[p]:
            start = p * p
            step = p
            is_prime[start:n + 1:step] = b"\x00" * (((n - start) // step) + 1)
        p += 1

    return [i for i in range(2, n + 1) if is_prime[i]]


def main():
    parser = argparse.ArgumentParser(description="Sieve of Eratosthenes (primes <= N).")
    parser.add_argument("N", type=int, help="upper bound (inclusive)")
    parser.add_argument("-p", "--print", action="store_true", help="print primes")
    parser.add_argument("-c", "--count", action="store_true", help="print number of primes")
    parser.add_argument("-f", "--file", nargs=1, help="CSV filename to save primes")
    args = parser.parse_args()

    N = args.N
    if N < 0 or N > 200_000_000:
        sys.exit("Error: N must be between 0 and 200,000,000 (adjust if you have RAM).")

    primes = sieve_eratosthenes(N)

    if args.count:
        print(len(primes))

    if args.print:
        print(primes)

    if args.file:
        filename = args.file[0]
        with open(filename, "w", encoding="utf-8") as f:
            f.write(",".join(map(str, primes)))
        print(f"Saved {len(primes)} primes to {filename}")


if __name__ == "__main__":
    main()

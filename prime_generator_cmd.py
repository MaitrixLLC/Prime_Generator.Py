# Prime Number Generator with command line arguments by Eric Olsen
# This is a prime number sieve which uses concept of residue numbers
import numpy as np
from numpy import asarray
from numpy import savetxt
import argparse
import sys

primes = np.array([2])         # start with the first prime
#print("starting primes array:", primes)
digits = np.array([0])         # start with first digit equal to zero

def contains_zero(array):
    for j in range(0, array.size):
        if array[j] == 0:
            return True
    return False
        
def wrap_digits(primes, digits):
    for i in range(primes.size):
        if(digits[i] == primes[i]):
            digits[i] = 0

parser = argparse.ArgumentParser()
parser.add_argument("cnt", type=int, help="the number of primes to generate starting with 2")  # mandatory?
parser.add_argument("-p", "--print", action="store_true", help="print primes to stdout")
parser.add_argument("-s", "--stats", action="store_true", help="print statistics to stdout")
parser.add_argument("-f", "--file", nargs=1, help="CSV formatted filename to save primes to")

            
args = parser.parse_args()    # get the arguments
number = args.cnt    # get the number of primes to generate
if(number < 1) or (number > 1000000):
    sys.exit("Error: cnt argument should between 1 and 1,000,000")
    
num_of_multiplies = 0
num_of_increments = 0
            
num_primes = 1
last = 2
print("Generating the first", number, "primes without any division:")
print("Please wait !")
while(num_primes < number):
    index = 0
    max_prime = primes[primes.size-1] ** 2   # MAX TRIAL DIGIT WILL BE LAST PRIME FOUND SQUARED
    num_of_multiplies += 1
    for trial in range(last+1, max_prime):
        digits += 1     # increment the digits array
        num_of_increments += digits.size
        wrap_digits(primes, digits)    # wrap the digits array against each digit's moduli (the primes array)
#        print("digits:", digits)      # THIS IS THE NATURAL RESIDUE NUMBER
        if not contains_zero(digits):
            primes = np.insert(primes, primes.size, trial)     # THE MODULI OF THE RESIDUE NUMBER IS EXTENDED BY THE NEW PRIME!
            digits = np.insert(digits, digits.size, 0)         # THE NEW DIGIT FOR THE NEW MODULUS INSERTED IS ALWAYS ZERO!  
            num_primes += 1
            if(num_primes >= number):
                break
    last = max_prime-1
    

if(args.print):    
    print("\n")
    print(primes)
if(args.stats):
    print("\n")
    print("total number of multiplications:", num_of_multiplies)
    print("total number of increments (and compares:)", num_of_increments)
if(args.file):
    save_data = asarray(primes)
    filename = args.file
    savetxt(filename[0], save_data, delimiter=',', fmt='%d')
    print("\n")
    print("primes saved to %s" % filename[0])

print("Primes Generation completed!")

import sys
import math
from tqdm import tqdm

primes = []

def is_prime(n):
	if n <= 1: 
		return False

	if n == 2 or n == 3:
		return True

	if (n % 10) % 2 == 0:
		return False

	for i in range(3, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False

	return True


def next_prime():
	n = 2
	while True:
		if is_prime(n):
			yield(n)
		n += 1

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("Invalid parameters!")
	else:
		N = int(sys.argv[1])
		prime_gen = next_prime() 
		for i in tqdm(range(N), ascii=True):
			primes.append(next(prime_gen))

		print('All primes: {}'.format(', '.join(map(str, primes))))
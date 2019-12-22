import sys
import math

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

primes = []

def is_prime(n):
	if n <= 1: 
		return False

	if n == 2 or n == 3:
		return True

	last_digit = n % 10

	if last_digit % 2 == 0:
		return False
	
	if last_digit == 5:
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

@app.route('/api/primes', methods=['GET'])
@cross_origin()
# Example: http://127.0.0.1:8889/api/primes?N=1000
def get_primes():
	args = request.args
	N = int(args['N'])
	primes = []
	prime_gen = next_prime()
	for i in range(N):
		primes.append(next(prime_gen))

	return jsonify(primes)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)
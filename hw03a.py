primes = []
for x in range (0, 10002):
	for i in range (2, x):
		if x % i == 0:
			break
	else:
		primes.append(str(x))
		
print primes
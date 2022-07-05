# Q) Sum of all primes below two million.

def isPrime(n):
	if n == 2 or n == 3:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False
	i = 5
	while i*i <= n:
		if n%i == 0 or n%(i+2) == 0:
			return False
		i += 6
		
	return True

print(sum([i for i in range(1, 2000000)]))

# Time Complexity - O(n^0.5)
# Space Complexity - O(1)

'''
Sample Input:

Sample Output:
142913828922
'''

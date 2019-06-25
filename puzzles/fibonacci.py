''' 
Fibonacci Series : 
In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation
	Fn = Fn-1 + Fn-2
with seed values 
	F0 = 0 and F1 = 1.
https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
'''

import time

# recursive version

def fibonacci(num):
	# return num if num <=1 else fibonacci(num-1) + fibonacci(num-2)
	if num in [0,1]:
		return num
	return fibonacci(num-1) + fibonacci(num-2)

# memoise version

cache = {}

def fibonacci_memoise(num):
	if num in cache:
		return cache[num]
	if num in [0,1]:
		val = num
	else:
		val = fibonacci_memoise(num-1) + fibonacci_memoise(num-2)
	cache[num] = val
	return val

# decorator 

def memoise(fun):
	cache = {}
	def wrapper(num):
		if num in cache:
			return cache[num]
		else:
			val = fun(num)
			cache[num] = val
			return val
	return wrapper

# non recursive

def fibonacci_non_recursive(num):
    a,b = 0,1
    for _ in range(num):
        a,b = b, a+b
    return a

if __name__=='__main__':

	start = time.time()
	for i in range(0, 30): # Higher input will take severe duplicate calculations
		print i, fibonacci(i)
	end = time.time()
	print 'Total Execution Time : {}'.format(end-start)
	time.sleep(1)

	start = time.time()
	for i in range(0, 1000):
		print i, fibonacci_memoise(i)
	end = time.time()
	print 'Total Execution Time : {}'.format(end-start)		
	time.sleep(1)

	start = time.time()
	fibonacci = memoise(fibonacci)
	for i in range(0, 1000):
		print i, fibonacci(i)
	end = time.time()
	print 'Total Execution Time : {}'.format(end-start)
	time.sleep(1)

	start = time.time()
	for i in range(0, 10): # Higher input will take severe duplicate calculations
		print i, fibonacci_non_recursive(i)
	end = time.time()
	print 'Total Execution Time : {}'.format(end-start)
	time.sleep(1)

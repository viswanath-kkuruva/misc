# https://www.geeksforgeeks.org/binary-search/

# find element in list using binary search
# assumption is list is in sorted order

# recursive method 

def binary_search_recursive(lst, num, start, end):
	if start <= end:
		mid = (start + end) // 2
		if lst[mid] == num:
			return mid
		elif lst[mid] > num:
			return binary_search_recursive(lst, num, start, mid-1)
		else:
			return binary_search_recursive(lst, num, mid+1, end)
	else:
		return -1

# iterative method

def binary_search_iterative(lst, num, start, end):
	while(start <= end):
		mid = (start + end) // 2
		if lst[mid]==num:
			return mid
		elif lst[mid]>num:
			end = mid-1
		else:
			start = mid+1
	return -1


lst = [5,19,12,18,13,17,16,14,15]
lst = sorted(lst)
print(lst)

num = 19
print('Recursive : {} is at index {}'.format(num, binary_search_recursive(lst, num, 0, len(lst)-1)))

num = 10
print('Recursive : {} is at index {}'.format(num, binary_search_recursive(lst, num, 0, len(lst)-1)))

num = 19
print('Iterative : {} is at index {}'.format(num, binary_search_iterative(lst, num, 0, len(lst)-1)))

num = 10
print('Iterative : {} is at index {}'.format(num, binary_search_iterative(lst, num, 0, len(lst)-1)))

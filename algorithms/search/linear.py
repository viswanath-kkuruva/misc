# https://www.geeksforgeeks.org/linear-search/

# find element in list using linear search

def linear_search(lst, num):
	pos = -1
	for indx, item in enumerate(lst):
		if item == num:
			pos = indx
			break
	return pos

lst = [1,9,2,8,3,7,6,4,5]

num = 6 
print('{} is at index {}'.format(num, linear_search(lst, num)))

num = 10
print('{} is at index {}'.format(num, linear_search(lst, num)))

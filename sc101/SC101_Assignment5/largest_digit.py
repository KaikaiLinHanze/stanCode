"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""
ans = -float("inf")


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: a integer
	:return: the biggest digit in 5 different integers
	"""
	global ans
	n = abs(n)
	n1 = n % 10
	n2 = n // 10 % 10
	if n == 0:
		largest = ans
		ans = -float("inf")
		return largest
	else:
		if n1 > n2:
			if n1 > ans:
				ans = n1
		return find_largest_digit(n//10)
		# base case 的處理


if __name__ == '__main__':
	main()

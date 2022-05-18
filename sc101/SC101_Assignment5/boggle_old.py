"""
File: boggle.py
Name: Kai
----------------------------------------
find all the anagram in the boggle.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dic = {}
count = 0


def main():
	"""
	find all the anagram in the boggle.
	"""
	read_dictionary()
	data = in_put_data()
	anagram = get_x_y_in_anagram(data)
	print(f'There are {len(anagram)} words in the boggle.')


def in_put_data():
	"""
	:return input data
	"""
	# correct_input = 0
	# while True:
	# 	row1 = input(f'1 row of letters : ').lower()
	# 	if len(row1) != 7:
	# 		break
	# 	row1 = row1.split(" ")
	# 	if len(row1) != 4:
	# 		break
	# 	row2 = input(f'2 row of letters : ').lower()
	# 	if len(row2) != 7:
	# 		break
	# 	row2 = row2.split(" ")
	# 	if len(row2) != 4:
	# 		break
	# 	row3 = input(f'3 row of letters : ').lower()
	# 	if len(row3) != 7:
	# 		break
	# 	row3 = row3.split(" ")
	# 	if len(row3) != 4:
	# 		break
	# 	row4 = input(f'4 row of letters : ').lower()
	# 	if len(row4) != 7:
	# 		break
	# 	row4 = row4.split(" ")
	# 	if len(row4) != 4:
	# 		break
	# 	correct_input += 1
	# 	break
	# if correct_input != 1:
	# 	print(f'Illegal input')
	# else:
	# 	word_list =[row1, row2, row3, row4]
	# 	return word_list
	words = [['f', 'y', 'c', 'l'], ['i', 'o', 'm', 'g'], ['o', 'r', 'i', 'l'], ['h', 'j', 'h', 'u']]
	return words


def get_x_y_in_anagram(data):
	"""
	input:data from user
	return: ans with anagram list.
	"""
	ans = []
	for i in range(4):
		for j in range(4):
			find_anagrams(i, j, data, [], ans)
	return ans


def find_anagrams(x, y, in_put_list, cur, answer):
	"""
	:param x: x index for the input digit
	:param y: y index for the input digit
	:param in_put_list: list, the entered listed of boggle
	:param cur: list, the temporary list for boggle calculation
	:param answer: list, the final list of boggle found
	"""
	# Base case
	if len(cur) == 4:
		current = repeat_index(cur, [])
		if len(current) == 4:
			word = ''
			for site in current:
				x_site = site[0]
				y_site = site[1]
				word += in_put_list[x_site][y_site]
			if word in dic and word not in answer:
				answer.append(word)
				print('Found: ' + word)
				return answer
	if len(cur) > 4:
		current = repeat_index(cur, [])
		if len(current) > 4:
			word = ''
			for site in current:
				x_site = site[0]
				y_site = site[1]
				word += in_put_list[x_site][y_site]
			if word in dic and word not in answer:
				answer.append(word)
				print('Found: ' + word)
				return answer
	else:
		# Choose
		cur.append([x, y])
		# Explore
		for i in range(-1, 2):
			for j in range(-1, 2):
				if i == 0 or j == 0:
					pass
				else:
					if 0 <= x + i <= 3 and 0 <= y + j <= 3:
						find_anagrams(x+i, y+j, in_put_list, cur, answer)
		# Un-choose
		cur.pop()


def repeat_index(in_put, index_memory):
	for site in in_put:
		if site not in index_memory:
			index_memory.append(site)
	return index_memory


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dic
	with open(FILE, mode="r") as f:
		for line in f:
			dic[line.strip()] = 0


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for ch in dic:
		if ch.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()

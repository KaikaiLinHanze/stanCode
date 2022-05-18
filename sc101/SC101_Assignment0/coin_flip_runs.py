"""
File: coin_flip_runs.py
Name: Kai
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the runs!
"""

import random as r


def main():
	"""
	TODO:
	"""
	runs = int(input("Let's flip a coin! \nNumber of runs : "))
	is_in_a_row = False
	old_flip = 0
	run_time = 0
	ans = ""
	while True:
		coin_flip = r.choices("HT")
		data = coin_flip[0]
		ans += data
		if old_flip == data:
			if is_in_a_row is False:
				run_time += 1
				is_in_a_row = True
		else:
			is_in_a_row = False
		old_flip = data
		if run_time == runs:
			break
	print(ans)

	# ans = ""
	# show = ""
	# new_data = 0
	# old_data = 0
	# run = 0
	# num_run = int(input("Let's flip a coin!\nNumber of runs:"))
	# while True:
	# 	coin_flip = r.randrange(1,3)
	# 	if coin_flip == 1:
	# 		new_data = "H"
	# 		show += new_data
	# 	if coin_flip == 2:
	# 		new_data = "T"
	# 		show += new_data
	# 	if old_data == new_data:
	# 		ans += new_data
	# 		if len(ans) == 1:
	# 			run += 1
	# 	else:
	# 		ans = ""
	# 	old_data = new_data
	# 	if run == num_run:
	# 		break
	# print(show)



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()

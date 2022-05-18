"""
File: weather_master.py
Name:
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100
COLD = 16


def main():
	print(f'stanCode\"Weather Master4.0\"!')
	collect_data = []
	while True:
		data = int(input("Next Temperature:(or" + str(EXIT) + "to quit)?"))
		if data == EXIT:
			break
		else:
			collect_data.append(data)
	print(f'Highest temperature{str(max(collect_data))}')
	print(f'Lowest temperature{str(min(collect_data))}')
	print(f'Average{sum(collect_data)/len(collect_data)}')
	cold_day = [ele for ele in collect_data if ele <= COLD]
	print(f'{len(cold_day)} cold day(s)')









# EXIT = -100
# COLD = 16
# def main():
# 	print("stancode weather")
# 	data = int(input("please type in a weather or" + str(EXIT) + " to quit"))
# 	if data == EXIT:
# 		print ("there is no data")
# 	else:
# 		hot = data
# 		cold = data
# 		sum = 0
# 		total_day = 0
# 		cold_day = 0
# 		while True:
# 			if data == EXIT:
# 				print ("the hottest day is:" + str(hot))
# 				print ("the coldest day is:" + str(cold))
# 				print ("average weather is:" + str(sum / total_day))
# 				print ("the cold day is " + str(cold_day))
# 				break
# 			if data > hot:
# 				hot = data
# 			if data < cold:
# 				cold = data
# 			if data < COLD:
# 				cold_day += 1
# 			sum += data
# 			total_day += 1
# 			data = int(input("please type in a weather or" + str(EXIT) + " to quit"))

# EXIT = -100
# COLD = 16
#
#
# def main():
# 	print("stanCode \"Weather Master 4.0\"!")
# 	collect = []
# 	while True:
# 		data = int(input("Next Temperature: ( or " + str(EXIT) + "to quit) ?"))
# 		if data == EXIT:
# 			break
# 		collect.append(data)
# 	print("Highest temperature = " + str(max(collect)))
# 	print("Lowest temperature =" + str(min(collect)))
# 	# cold_day = list(ele for ele in collect if ele <= COLD)
# 	cold_day = [ele for ele in collect if ele <= COLD]
# 	print("Average = " + str(sum(collect)/len(collect)))
# 	print(str(len(cold_day)) + " cold day(s)")

###### DO NOT EDIT CODE BELOW THIS LINE ######


if __name__ == "__main__":
	main()

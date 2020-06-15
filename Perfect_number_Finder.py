num = int(input()) # Taking Number Upto perfect Numbers are To Be found
perfect_nums = []
for i in range(1,num+1):
	factors = []
	factors_sum = 0
	for n in range(1,i):
		if i % n == 0:
			factors.append(n)
	for factor in factors:
		factors_sum += factor
	if factors_sum == i:
		perfect_nums.append(i)
print("Perfect Numbers Upto " + str(num) + ": " , perfect_nums)
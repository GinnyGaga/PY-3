i=0
numbers=[]

for i in range(6):
	print("At the top i is %d" % i)
	numbers.append(i)
#	i=i+1
	print("Numbers now:",numbers)
	print("At the bottom i is %d" % i)


print("The numbers:")
numbers=range(6)
for num in numbers:
	print (num)
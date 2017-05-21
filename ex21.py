def add(a,b):
	print ("ADDING %d+%d" % (a,b))
	return a+b

def subtract(a,b):
	print("SUBTRACTING %d - %d" % (a,b))
	return a-b

def multiply(a,b):
	print("MULTIPLYING %d * %d" % (a,b))
	return a*b

def divide(a,b):
	print("DIVIDING %d / %d" % (a,b))
	return a/b

print ("Let's do some math with just functions!")

age=add(30,5)
height=subtract(78,4)
weight=multiply(90,2)
iq=divide(100,2)

print("Age:%d,Height:%d,Weight:%d,IQ:%d" % (age,height,weight,iq))

print("Here is a puzzle.")

#what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print ("iq=%d" % iq)

f1=divide(iq,2)
print ("f1=divide(iq,2)=%d" % f1)

print ("weight=%d" % weight)

f2=multiply(weight,f1)
print('f2=multiply(weight,f1)=%d' % f2)


print('height=%d' % height)

f3=subtract(height,f2)
print('f3=subtract(height,f2)=%d' % f3) 

print('age=%d' % age)

f4=add(age,f3)
print('f4=add(age,f3)=%d' % f4)











#print("That becomes:",what,"Can you do it by hand?")







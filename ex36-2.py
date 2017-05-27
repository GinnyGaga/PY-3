from sys import exit
from sys import argv

def txt():
	print("you should read the instruction before the festival.")
	script,filename=argv
		
	test=open(filename)
	print(test.read())	
	print(test.close())
	plan()

def play():
	print("so,how much money do you have?")
	next=input(">")
	
	if "0" in next or "1" in next:
		how_much=int(next)
	else:
		quit("just type the money you have.")

	if how_much > 100:
		print("I'll go to Disney myself.")
		exit(0)
	else:
		quit("you are the poor.")
		

def he():
	print("But how is him?")
	not_available=False

	while True:
		next=input(">")
		if "love" in next:
			print("I love you ,too.")

		elif "happy" in next and not not_available:
			print("we can date!!!")

			not_available=True
		elif "happy" in next and not_available:
			print ("it is the same!")
		else:
			print("excuse me?")

def plan():
	print("it is not raining,so i have two plan.")
	plan=input(">")

	if "date" in plan:
		print("I'll date with him.")
		he()
	elif "play" in plan:
		print("I have to play myself.")
		play()
	else:
		start()
def rain():
	print("what's the weather?")
	weather=input(">")

	if "not_rain" == weather:
		print("I am so happy!")
		txt()
	else:
		print("I go to sleep.")
		exit(0)

def quit(why):
	print(why,"you!!")
	exit(0)
def start():
	print("are you over_worked or not over_worked?")
	chooce=input(">")

	if "not" in  chooce:
		print("I have festivel!")	
		rain()
	else:
		print("I have no festivel.")
		exit(0)
start()

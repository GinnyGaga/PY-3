from sys import exit

def play():
	print("so,how much money do you have?")
	money=input(">")
	
	if "0" in money or "1" in money:
		how_much=int(money)
	else:
		quit("just type the money you have.")

	if how_much < 100:
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
			quit("fuck!")

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
		print("excuse me? what are you want to say?")

def rain():
	print("what's the weather?")
	weather=input(">")

	if "not_rain" == weather:
		print("I am so happy!")
		plan()
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

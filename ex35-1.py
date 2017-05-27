from sys import exit

def gold_room():
	print("How much gold do you take?")
	next=input(">")
	
	#if "0" in next or "1" in next:
	if True:
		 print (next.isdigit())
		 how_much=int(next)
	else:
		dead("Man,learn to type a number.")


	if how_much< 50:
		print("Nice,you're not greedy,you win!")
		exit(0)
	else:
		dead("you dead!")


def bear_room():

	print("How to move the bear?")

	bear_moved=False  #

	while True:
		next=input(">")
	
		if next == "money":
			dead("you dead!")
		elif next == "taunt" and not bear_moved:
			print("you can chooce to open door or taunt bear again.")

			bear_moved=True
		elif next =="taunt" and bear_moved:
			dead("you dead!") 
		elif next == "open" and bear_moved:
			gold_room()
		else:
			print("what?")


def cthulhu_room():

	print("it's the cthulhu room,flee your life or eat your head?")

	next=input(">")
	
	if "f" in next:
		start()
	elif "h" in next:
		dead("you dead!")
	else:
		cthulhu_room()
	

def dead(why):
	print(why,"Good job!")
	exit(0)

def start():  
	print("Which door do you take?")

	next=input(">")
	
	if next =="l":
		bear_room()
	elif next== "r":
		cthulhu_room()
	else:
		dead("You dead!")

start()



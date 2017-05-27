from sys import exit

def gold_room():
	print("This room is full of gold.How much do you take?")
	next=input(">")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man,learn to type a number.")


	if how_much <50:
		print("Nice,you're not greedy,you win!")
		exit(0)
	else:
		dead("You greedy bastard!")


def bear_room():
	print("There is a bear hear.")
	print("The bear has a bunch of honey.")
	print("The fat bear is in front of another door.")
	print("How are you going to move the bear?")
	bear_moved=False  #

	while True:
		next=input(">")
	
		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print("The bear has moved from the door.You can go throught it now.")

			bear_moved=True
		elif next =="taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.") 
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print("I got no idea what that means.")


def cthulhu_room():
	print("Here you see the great evil cthulhu.")
	print("He,it,whatever stares at you and you go insane.")
	print("Do you flee your life or eat your head?")
	

	next=input(">")
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("well that was tasty!")
	else:
		cthulhu_room()
	

def dead(why):
	print(why,"Good job!")
	exit(0)

def start():  #整个脚本最先执行的部分
	print("You are in a dark room.")
	print("There is a door to your right and left.")
	print("Which one do you take?")

	next=input(">")
	
	if next =="left":
		bear_room()#若填入left,转向bear_room
	elif next== "right":
		cthulhu_room()#若填入right,则转向cthulhu_room
	else:
		dead("You stumble around the room until you starve.")#若什么都不填，或则填别的，则转向dead(why):提示你会饿死，退出。

start()#在脚本的结尾写明整个脚本要开始的位置。



def start():
	print("there are two heroes that you can choose:tiger and cat.")
	print("you can chooce one of them.")
	animals=input(">")
	
	if animals == "tiger":
		tiger()
	elif animals == "cat":
		cat()
	else:
		dead("you so week.")

def tiger():
	print("Now,you have an equipment:equip1")
	you_hurt=False

	while True:
		equip=input(">")
	
		if "1" in equip and not you_hurt:
			print("you  kill the enemy.")
			start()
		
		elif "1" in equip and you_hurt:
			print("you kill the enemy.")
			start()

		else:
			dead("you'll be killed.")

def cat():
	print("now,you're in front of a room with too much money.")
	print("how much you will take?")
	
	money=input(">")
	
	if True:
		print(money.isdigit()) 
		how_money = int(money)
	else:
		dead("type a number again.")
	
	if how_money <100:
		print("you are a good man.")
		exit(0)
	elif 100 < how_money <110:
		tiger ()
	else:
		dead("you dead.")

def dead(why):
	print(why,"Haha!!!")
	exit(0)

	
start ()

from sys import exit
from random import randint

def death():
	quips=["You died.You kinda suck at this.",
		"Nice job,you died ...jackass.",
		"Such a luser.",
		"I have a small puppy that's better at this."]
	print (quips[randint(0,len(quips)-1)])
	exit(1)

def central_corridor():
	
	action=input(">")

	if action == "shoot!":
		return 'death'

	elif action =="dodge!":
		return 'death'

	elif action=="tell a joke":
		return 'laser_weapon_armory'
		
	else:
		print("DOES NOT COMPUTE!")
		return 'central_corridor'
def laser_weapon_armory():

	code = "%d%d%d"% (randint(1,9),randint(1,9),randint(1,9))
	
	guess=input("[keypad]>")
	guesses=0

	while guess != code and guesses <10:
		print("BZZZZEDDD!")
		guesses +=1
		guess=input("[keypad]>")

#how to connet while-loop to if-loop?

	if guess == code :  #why it fails to work?
		return 'the_bridge'

	elif guess == "got it":
		print("good job!")
		return 'money'

	else:
		return 'death'
def money():
	print("you will have much money")
	print("and how much will you get:")
	
	how_much = input(">")
	
	if "0" in how_much or "1" in how_much:
		how_muchA=int(how_much)
	
	else:
		return 'death'

	if how_muchA > 100:
		print("you did the good job")
	else:
		exit(0)


def the_bridge():

	action = input(">")

	if action == "throw the bomb":
		return 'death'

	elif action == "slowly place the bomb":
		return 'escape_pod'

	else:
		print("DOES NOT COMPUTE!")
		return("the_bridge")
def escape_pod():

	good_pod=randint(1,5)
	guess=input("[pod#]>")
	
	if int(guess) != good_pod:
		return 'death'
	else:
		exit(0)

ROOMS ={
	'death':death,
	'central_corridor':central_corridor,
	'laser_weapon_armory':laser_weapon_armory,
	'the_bridge':the_bridge,
	'escape_pod':escape_pod
}

def runner (map,start):
	next =start

	while True:
		room=map[next]
		print("\n-------")
		next = room()

runner(ROOMS,'central_corridor')

	

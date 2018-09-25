#This is the dice total guessing game
from random import randint
from time import sleep
def get_user_guess():
	guess = int(raw_input("What's your guess?: "))
	return guess
def roll_dice(number_of_sides):
	first_roll = randint(1,number_of_sides)
	second_roll = randint(1,number_of_sides)
	max_val = number_of_sides * 2
	print "This is the dice guessing game"
	print "The maximum value is %d" % max_val 
	guess = get_user_guess()
	if guess > max_val:
		print "Your guess is invalid"
	else:
		print "Rolling..."
		sleep(2)
		print "The first roll is %d" % first_roll
		print "Rolling..."
		sleep(3)
		print "The second roll is %d" % second_roll
		print "Calculating total..."
		sleep(3)
		total_roll = first_roll + second_roll
		print "Your total is %d" % total_roll
		print "Result..."
		sleep(4)
		if guess == total_roll:
			print "YOU WON!"
		else:
			print "%d does not equal %d. Uh oh...you lost :/" % (total_roll,guess)
roll_dice(6)
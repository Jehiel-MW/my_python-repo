import random as rd
import time


print('Welcome To Our Number Guess Game!!!\n\n')

time.sleep(1)

name = input("What can we call you: ")

print("\nHello,", "\033[35m",name.capitalize(), "\033[0m")

resp = {'yea':1, 'oui':2, 'beni':3, 'yes':4, 'yeah': 5, 'yep': 6}

print("\n\n Are you ready")

ans = input('\n\nType in a positive answer if you are ready: ')

if ans not in resp:
	exit()
time.sleep(1)

print("\n\nWelcome","\033[032m",name.capitalize(), '\033[0m\n')
time.sleep(1)
print('You are in for an adventure')

questSec = input('\n\nCan you do a number guessing: ')

if questSec not in resp:
	exit()
	
time.sleep(1)
print("\nLet's get started")

test = 1234
time.sleep(1)
userInput = input("\nEnter four digit: ")
userInt = int(userInput)
myInput = rd.randint(1000, 9999)
if((test == userInt) | (userInt == myInput) ):
	print("\033[036m",name.capitalize(), '\033[0m',"You won!")
else:
	print("\033[036m",name.capitalize(), '\033[0m', 'Try again')

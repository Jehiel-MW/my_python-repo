#The purpose of this program is to accept input from user's
#It is also to create a Story based on the information generated from the users
#It has a time dealing function to make the program fun to relate with
#Try to make fun out of this


import time
print("""This page will take in your information
The information will be used to create a story for you
Have fun with this...""")

time.sleep(1)

print("\nAre you ready?")

resp = input(str('Enter a response: '))
ans = {'yes':1, 'yea':2, 'yeah':3, 'yep':4, 'beni':5}
if resp not in ans:
					exit()

time.sleep(2)
name = input("\nEnter your first name: ")
adTit = input("\nEnter the title of your adventure: ")

locat = input("\nWhere do you live: ")
age = input("\nHow old are you: ")
job = input("\nWhat is your occupation: ")
fav = input("\nList the things you love doing: ")
do = input("\nWhat is that thing you can't stop doing: ")
amb = input("\nWhat is your ambition: ")

print("\n\n\n composing your story\n")

time.sleep(3)

print("Welcome to", name + '\'s', "Adventure of", adTit)
print("\n\n\033 My is ", name, "I am", age, "year's old I live in", locat + '.')
print('I work as a/n', job, 'currently and I love (to)', fav + '.', "I can't just stop", do + ',', "I have an ambition to be a/an", amb, 'all of my life.')

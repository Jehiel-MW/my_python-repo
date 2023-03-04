from statistics import mean as m, mode as md

# This is to take in the admin section login procedure as it is a database which should be privately managed

admin = {"aojo@oa" : "bath2#", "oade@oa":"+2gets", "admin":"abcdef", "ala@oa":"123gets", "a":"1"}


	
# This is the define function to manage adding a new student and/or grade to the database



student = {}


def enterGrade():
		nameToenter = input("Student Name: ")
		gradeToenter = input("Grade: ")
		if nameToenter in student:
			print("Adding grade....")
			student[nameToenter].append(gradeToenter)
		else:
			print("Student's data not in the Database...")
		print(student)
		

#This line of code is defined to add new student to the database
	
			
def newStudent():
		nameToenter = input("Student Name: ")
		gradeToenter = input("Grade: ")
		if nameToenter not in student:
			print("Adding new student to database...")
			student[nameToenter] = [gradeToenter]
		print(student)

# This is for removing student from the database, it is a define function that can be call upon anytime

def removeStudent():
	nameToremove = input("Withdrawn Student: ")
	if nameToremove in student:
		print("Removing student's data")
		del student[nameToremove]
	print(student)

def studentAvgs():
	for eachStudent in student:
		gradelist = student[eachStudent]
		avGrade = m(gradelist)
		print(eachStudent, "has an average of: ", avGrade)

def overallStudent():
	for allStudent in avGrade:
		bestStudent = md(avGrade)
		print(bestStudent)


# This is a define function to manage the welcome page

def main():
	print("""
	Welcome to Central Grading System
	
	
	[1]   -   New Student Data
	[2]   -   Enter Student Grade
	[3]   -   Remove Student Data
	[4]   -   Enter Student Grade
	[5]   -   Overall Best Student
	[6]   -   Exit
	""")
	
	action = input("Select the option task to complete(Enter a digit): ")
	if action == "1":
		newStudent()
	elif action == "2":
		enterGrade()
	elif action == "3":
		removeStudent()
	elif action == "4":
		studentAvgs()
	elif action == "5":
		overallStudent()
	elif action == "6":
		exit()
	else:
		print("You have make the wrong choice, try again")



login = input("Username: ")
passwd = input("Password: ")

if login in admin:
		if admin[login] == passwd:
			print(login, "Welcome to Student Database")
			while True:
				main()
		else:
			print("Invalid password, attempt after 30mins")
else:
	print("Username name not recognise, reporting to admin management")

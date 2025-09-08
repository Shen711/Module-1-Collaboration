#Nathan Schoenike
#Module 2 Case Study Assignment
#Purpose: To determine if a student has made the Dean's list or Honor Roll based on their GPA.

import sys
#variables are just students names and GPA
studentLastName = input("Please enter the students last name: ")

while studentLastName != "ZZZ":
    if studentLastName == "ZZZ":
        print("Exiting the program.")
        sys.exit()
    studentFirstName = input("Please enter the students first name: ")
    studentGPA = float(input("Please enter the students GPA: "))
    if studentGPA >= 3.5:
        print(studentFirstName + " " + studentLastName + " has made the Dean's list.")
    elif studentGPA >= 3.25 and studentGPA < 3.5:
        print(studentFirstName + " " + studentLastName + " has made the Honor Roll.")
    else:
        print(studentFirstName + " " + studentLastName + " has a GPA of " + str(studentGPA) + ".")
    studentLastName = input("Please enter the students last name: ")    


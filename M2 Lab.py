"""
Name:  Emma Foust
Filename: M2 Lab.py
Description: This program asks for the student's name and GPA. The program ends if the student's last name
is entered as 'ZZZ', and the GPA must be entered as a float, or as an interger that can be converted into a float.
The program displays whether or not the student made the Dean's list or Honor Roll, based on their GPA. 

"""

lastname = input("Enter Student's Last Name: ")
if lastname != "ZZZ":
    firstname = input("Enter Student's First Name: ")
    gpa = input("Enter Student's GPA: ")
    gpa = float(gpa)
    if gpa > 3.5:
        print(f"{firstname} {lastname} has made the Dean's List.")
    elif gpa > 3.25:
        print(f"{firstname} {lastname} has made the Honor Roll.")
    else:
        print(f"{firstname} {lastname} did not make the Honor Roll or Dean's List." )
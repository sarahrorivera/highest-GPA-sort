'''
This program is used to take input from a user to determine
which student in the class has the highest GPA
Author: 
Sarah Rivera 
'''

#create a class for the exception of the empty roster 
class EmptyRosterError(Exception):
    pass

#create a class for students seperating the first name, last name, and GPA
class Student:

#define a function for these labels
    def __init__(self, first, last, gpa):

        self.first = first

        self.last = last

        self.gpa = gpa


#define a function for first name, return the output
    def get_first(self):

        return self.first


#define a function for last name, return the output
    def get_last(self):

        return self.last

#define a function for GPA, return the output 
    def get_gpa(self):

        return self.gpa


#create a class for course, define functions to seperate course size as well as the highest gpa
class Course:

    def __init__(self):

        self.roster = []



    def add_student(self, student):

        self.roster.append(student)



    def course_size(self):

        return len(self.roster)


#(this is the function for finding highest gpa)
    def find_student_highest_gpa(self):
#EXCEPT..........
        if not self.roster:

            raise EmptyRosterError('Exception: Course Roster is Empty')

        return max(self.roster, key=lambda student: student.get_gpa())

#define main function 
def main():
#create a class for course
    course = Course()

    
#create loops, quit to break them
    while True:

        print("welcome to CSC/DSCI: principles in CS/DS I")

        print("please add students to the course: ")


#collect user input
        first_name = input("enter first name:> ")

        
#break loop if exit command detected 
        if first_name.lower() == 'quit':

            break


#collect user input 
        last_name = input("enter last name: ")

        
#try + exceptions for non numeric GPA
        try:

            gpa = float(input("enter GPA:> "))

        except ValueError:

            print("Error: Enter a Numeric GPA")

            continue


#class for sudents first and last name 
        student = Student(first_name, last_name, gpa)

        course.add_student(student)


#determine course size based on the number of responses
    print(f"course Size: {course.course_size()} students")

    
#try + exceptions for student with the top GPA 
    try:

        best_student = course.find_student_highest_gpa()

        print(f"Top Student: {best_student.get_first()} {best_student.get_last()} (GPA: {best_student.get_gpa()})")
#create empty exception
    except EmptyRosterError as e:

        print(e)


#call to main function, if true function will perform
if __name__ == "__main__":

    main()

# Phyllis Torres
# Classes and Objects
# due November 3, 2016

# create a class of student information
class Student(object):
    """
    This class will contain student information
    """

# create instance of the class Student
studentInfo = Student()

studentInfo.studentID = "0190244"
studentInfo.firstName = "John"
studentInfo.lastName = "Cleese"
studentInfo.email = "jcleese@montypython.com"

# this code will allow a user to input the data to create an instance of Student
def create_student():
    s = Student()
    s.studentID = raw_input("\nEnter student Id number")
    s.firstName = raw_input("\nEnter student first name")
    s.lastName = raw_input("\nEnter student last name")
    s.email = raw_input("\nEnter student email address")
    return s

# call routine to create an instance of student
student1 = create_student()

# call routine to create an instance of student
student2 = create_student()

# print out the Student instances information
print ("\n\n" + studentInfo.studentID + ' ' + studentInfo.firstName + ' ' + studentInfo.lastName + ' ' + studentInfo.email + "\n\n")

print ("\n" + student1.studentID + ' ' + student1.firstName + ' ' + student1.lastName + ' ' + student1.email + "\n\n")

print ("\n" + student2.studentID + ' ' + student2.firstName + ' ' + student2.lastName + ' ' + student2.email + "\n\n")

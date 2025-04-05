# Claire Francis, April 4, 2025, Week10_program2
# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.

# Once you have written the class, write a program that creates three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.

class Employee:
    def __init__(self, Name, ID_Number, Department, Job_Title):
        self.__name = Name
        self.__ID_number = ID_Number
        self.__Department = Department
        self.__Job_Title = Job_Title

    def get_name(self):
        return self.__name

    def get_ID(self):
        return self.__ID_number

    def get_department(self):
        return self.__Department

    def get_title(self):
        return self.__Job_Title

from Employee import Employee

def main():

    employee1 = Employee("Susan Meyers", "47899", "Accounting", "Vice President")
    employee2 = Employee("Mark Jones", "39119", "IT", "Programmer")
    employee3 = Employee("Joy Rogers", "81774", "Manufacturing", "Engineer")

    print(employee1.get_name())
    print(employee1.get_ID())
    print(employee1.get_department())
    print(employee1.get_title())

    print(employee2.get_name())
    print(employee2.get_ID())
    print(employee2.get_department())
    print(employee2.get_title())

    print(employee3.get_name())
    print(employee3.get_ID())
    print(employee3.get_department())
    print(employee3.get_title())

if __name__ == '__main__':
    main()

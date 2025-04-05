# Claire Francis, April 4, 2025, Week10_program2
# Program # 2: Car Class
# Write a class named Car that has the following data attributes:

# __year_model (for the car's year model)
# __make (for the make of the car)
# __speed (for the car's current speed)
# The Car class should have an __init__ method that accepts the car's year model and make as arguments.  These values should be assigned to the object's __year_model and __make data attributes.  It should also assign 0 to the __speed data attribute.

# The class should also have the following methods:

# The accelerate method should add 5 to the speed data attribute each time it is called.
# The brake method should subtract 5 from the speed data attribute each time it is called.
# The get_speed method should return the current speed.
# Next, design a program that creates a Car object then calls the accelerate method five times.  After each call to the accelerate method, get the current speed of the car and display it.  The call the brake method.  After each call to the brake method, get the current speed of the car and display it.
class car:
    def __init__(self, make, yearmodel, speed):   # begins with initialization or constructor
        self.__make = make
        self.__year_model = yearmodel
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5


    def get_speed(self, speed):
        return self.__speed

from Week10_program2 import car

def main():
    make = input("Enter the make of car: ")
    yearmodel = input("Enter year of car model: ")
    speed = 0
    my_car = car(make, yearmodel, speed)

    my_car.accelerate()
    print("My speed is: ", my_car.get_speed(speed))

    my_car.accelerate()
    print("My speed is: ", my_car.get_speed(speed))

    my_car.accelerate()
    print("My speed is: ", my_car.get_speed(speed))

    my_car.accelerate()
    print("My speed is: ", my_car.get_speed(speed))

    my_car.accelerate()
    print("My speed is: ", my_car.get_speed(speed))

    my_car.brake()
    print("My speed is: ", my_car.get_speed(speed))

    my_car.brake()
    print("My speed is: ", my_car.get_speed(speed))

    my_car.brake()
    print("My speed is: ", my_car.get_speed(speed))

    my_car.brake()
    print("My speed is: ", my_car.get_speed(speed))

    my_car.brake()
    print("My speed is: ", my_car.get_speed(speed))
if __name__ == '__main__':
    main()



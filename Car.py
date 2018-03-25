# Class Written by Corey Seal
# Car.py Class
# March 25th 2018


class Car:                                      # car Class
    def __init__(self, year_model, make):       # init method with year_model & make accepted as arguments
        self.__year_model = year_model          #
        self.__make = make                      #
        self.__speed = 0                        # initializes the speed variable

    def get_speed(self):                        # display Speed Method
        return self.__speed                     # returns value in get_speed

    def accelerate(self):                       # accelerate Method
        self.__speed += 5                       # adds 5 to the speed variable

    def brake(self):                            # brake Method
        self.__speed -= 5                       # subtracts 5 from speed variable


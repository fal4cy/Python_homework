# Program Written by Corey Seal
# Exercise #2
# Accelerate / Brake Loops
# w/ Speed Display iterations
# March 25th 2018


import Car                                                  # import car class


def main():                                                 # main function
    yr_model = input('Enter Model Year: ')                  # input for model_year
    make = input('Enter Vehicle Make: ')                    # input for make

    vehicle = Car.Car(yr_model, make)                       # creates vehicle object

    for count in range(1, 6):                               # for loop counting 5 times
        vehicle.accelerate()                                # accelerates
        print('The current speed: ', vehicle.get_speed())   # print current speed on acc

    for count in range(1, 6):                               # for loop counting 5 times
        vehicle.brake()                                     # applies brakes
        print('The current speed: ', vehicle.get_speed())   # print current speed on brake


main()                                                      # call main function

#!/usr/bin/env python3

# Created by: Roman Cernetchi
# Created on: January 2021
# This program rounds a decimal

import math


def decimalRound(user_num, dec_place):
    # rounds a decimal

    # process
    user_num[0] = user_num[0] * (10 ** dec_place[0]) + 0.5
    user_num[0] = int(user_num[0])
    user_num[0] = user_num[0] / (10 ** dec_place[0])


def main():
    # input the number and height

    # list
    user_num = []
    dec_place = []

    while True:
        try:
            user_number = float(input("Enter the number you want to"
                                      " round: "))
            user_DecP = int(input("Enter how many decimal places to"
                                  " want to round to: "))
            print("")

            # list adding
            user_num.append(user_number)
            dec_place.append(user_DecP)

            # calls function
            decimalRound(user_num, dec_place)

            if user_number <= 0 or user_DecP <= 0:
                print("Invalid input")
            else:
                # ouput
                print("The rounded number is {}".format(user_num[0]))
                break

        except ValueError:
            print("This was not a number, try again.")


if __name__ == "__main__":
    main()

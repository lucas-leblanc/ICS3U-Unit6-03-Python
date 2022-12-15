#!/usr/bin/env python3

# Created by: Lucas LeBlanc
# Created on: Dec 2022
# This program finds the smallest number is an array of randomly generated numbers

import random


def finding_number(random_list):
    # This function finds smallest number

    smallest_number = random_list[0]
    for element in random_list:
        if element < smallest_number:
            smallest_number = element

    return smallest_number


def main():

    generated_random_list = []

    print("Here is a list of random numbers:")
    print("")

    for counter in range(0, 10):
        random_number = random.randint(1, 100)
        generated_random_list.append(random_number)
        print("The random number {0} is: {1}".format(counter + 1, random_number))

    smallest_number = finding_number(generated_random_list)
    print("\nThe smallest number is {0}".format(smallest_number))

    print("\nDone.")


if __name__ == "__main__":
    main()

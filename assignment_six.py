# Jack Fones
# 11-30-23
# This code runs a simulation in which 23 people are in a room. the simulation tests to see whether two people have the
# same birthday. The simulation will run however many times the user specifies and will tell the user what percent of
# the time there were duplicate birthdays.
import random


def get_birthdays():
    """
    creates a random list of 23 numbers between 1 and 365, which will serve as the birthdays.
    :return: list of 23 random numbers
    """
    return [random.randint(1, 365) for w in range(23)]   # Makes a list of 23 random numbers between 1 ad 365, each of which will represent a birthday.


def is_duplicates(birthdays):
    """
    tests to see whether there are duplicate birthdays
    :param birthdays: the random list of numbers
    :return: returns true or false, indicating whether there are duplicates.
    """
    for x in range(len(birthdays)):                             # This line creates the outer loop. "x" will take on each variable in the list every time it goes through the loop.
        for y in range(x + 1,len(birthdays)):                   # This line creates the nested loop. the variable "y" will take on each variable except for the one that is assigned to x, so that the numbers are not compared to themselves.
            if birthdays[x] == birthdays[y]:                    # Tests to see if the two variables, which each have a birthday assigned to them, are equal.
                return True
    return False                                                # These two lines will indicate to the code later whether there are repeats.


def main():
    duplicate_count = 0
    print("This code simulates a test in which 23 random people are placed in a room.")  # Explains what the code does to the user
    print("")
    print("The odds that two of those people share the same birthday is about 50%!")
    print("")
    print("Try it for yourself!")
    print("")
    try:
        simulation_count = int(input("How many times would you like to simulate this problem? "))    # The variable simulation_count will later tell the code how many times to make a list and test said list.
    except ValueError:                                                                               # This is a failsafe, which will trigger if the user does not enter a valid integer. If it triggers the code will just run again.
        print("Invalid input. Please enter a valid number.")
        return main()                                                                                # Reruns main

    for z in range(simulation_count):                                                   # This creates another loop that will run the amount of times the user entered. this loop is where all the code is called basically
        birthdays = get_birthdays()                                                     # Assigns the list to the variable birthdays.
        if is_duplicates(birthdays):                                                    # If is_duplicates returned true, the code will add one to the tally of duplicates.
            duplicate_count += 1

    percentage = round((duplicate_count / simulation_count) * 100,2)                    # Calculates the percentage and rounds it to the nearest hundredth.
    print(duplicate_count, "times there were two of the same birthday.")
    print("")
    print("This is about", percentage, "percent of the time.")
    print("")

    rerun = input("would you like to rerun the simulation? (y/n): ")
    if rerun == "y":
        main()
    elif rerun == "n":
        print("Thanks for playing!")
    else:
        another_rerun = input("Sorry, I don't understand. Please type y or n: ")       # If the user doesn't enter y or n the first time, it gives them one more chance.
        if another_rerun == "y":
            main()
        elif another_rerun == "n":
            print("Thanks for playing!")
        else:
            print("I still don't understand, sorry! Thanks for playing!")               # If they give two invalid inputs, the code just stops.


if __name__ == "__main__":
    main()

# Daniel Thompson, danielt5@usc.edu
# ITP 115, Fall 2021
# Section: 31865
# Assignment 1
# Description:
# This program displays two truths and a lie.

def main():

    #string variables

    first = "Daniel"
    last = "Thompson"
    statement1 = "I like to cook"
    statement2 = "I like to run"
    statement3 = "I am from Chile"

    #boolean variables

    truth1 = True
    truth2 = True
    truth3 = False

    #integer variables

    pets = 2
    siblings = 1

    #print of Full Name using variables (first = Daniel) and (last = Thompson). \n is used to create space between this and the next print statement

    print("Full Name:", first, last, '\n')

    #Print of # of pets and # of siblings using (pets = 2) and (siblings = 1). \n is used to create space between this and the next print statement

    print("Number of pets:", pets)
    print("Number of siblings:", siblings, '\n')

    #Print of all three statements using the variables statement1, statement2, and statement3. \n is used to create space between this and the next print statement

    print("Statement 1:", statement1)
    print("Statement 2:", statement2)
    print("Statement 3:", statement3, '\n')

    #Print of the truth and false statements using the boolean variables truth1, truth2, and truth3.

    print("Statement 1 is", truth1)
    print("Statement 2 is", truth2)
    print("Statement 3 is", truth3)

main()
#print ""
import os
import random

def main():

    userName = raw_input("whats your name?  ")

    randomNum = random.randrange(200)
    userGuess = ""

    messagesFile = open("motivation.txt","r")
    motivationList = messagesFile.read().splitlines()
    messagesFile.close()

    userMotivations = map(lambda motivation: "** " + motivation + ", "+ userName + "! **", motivationList)


    while userGuess != randomNum:
        #get the users userGuess
        #compare guess against randomNumber
        userGuess = int(raw_input("your guess "))
        if userGuess < randomNum:
            print (random.choice(userMotivations))
            print("your guess was too low ")
        elif userGuess > randomNum :
            print (random.choice(userMotivations))
            print("your guess was too high")
    print("*****")

    raw_input()

main()

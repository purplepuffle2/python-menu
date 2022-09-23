
import random

#global
people = []

#classes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


#functions

def rockPaperScissors():
        possibleActions = ["rock", "paper", "scissors"]
        
        losesTo = {
            "rock" : "scissors",
            "paper" : "rock",
            "scissors" : "paper"
        }

        def AI():
            AIChoice = random.choice(possibleActions)
            print("AI choice: " + AIChoice)
            return AIChoice

        def play(playerChoice, AIChoice):

            if(AIChoice == losesTo[playerChoice]):
                return "Player wins!"
            if(playerChoice == losesTo[AIChoice]):
                return "AI wins!"
            if(playerChoice == AIChoice):
                return "Draw!"

        playerChoice = input("\nRock, Paper, Scissors: ").lower()
        if playerChoice in possibleActions:
            print(play(playerChoice, AI()))
        else:
            print("Unknown option")


def menu():
    while(True): #menu
        print("\nOptions:\n1 - Basic test\n2 - Add person\n3 - Remove person\n4 - Clear array\n5 - Print people\n6 - Rock Paper Scissors")
        option = input("Enter option: ")
        print("\n")

        if(option == "1"):
            print("Hey welcome to basic test")

        elif(option == "2"):

            name = input("Enter your name: ")
            age = input("Enter your age: ")

            p = Person(name, int(age))
            people.append(p)
        
        elif(option == "3"):
            print("Removed " + people.pop().name)
        
        elif(option == "4"):
            people.clear()
            print("Array cleared")

        elif(option == "5"):
            #print("----------")
            for p in people:
                print("Name: " + p.name +"\nAge: " + str(p.age) + "\n----------")
        
        elif(option == "6"):
            rockPaperScissors()


        elif(option == "exit"):
            break

        elif(option == "secret"):
            print("Wow! You found the secret option! There is nothing here to see, here is a cat:\n₍=୪ Ⱉ ୪=₎")


        else:
            print("Error: Unknown option")



#starts here
print("Heyy welcome to my program :3")
menu()

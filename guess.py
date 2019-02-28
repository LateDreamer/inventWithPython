# This is the Guess The Number game
import random

chanceTaken=0
userName=input('Hello! What is your name?')
print('Well, '+userName+' I am thinking of a number between 1 and 20.')
randomNumber = random.randint(1,20)

for i in range(6):
    guessedNumber=input('Take a guess')
    

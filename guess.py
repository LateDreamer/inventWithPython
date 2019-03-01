# This is the Guess The Number game
import random

chanceTaken=0
userName=input('Hello! What is your name?')
print('Well, '+userName+', I am thinking of a number between 1 and 20.')
randomNumber = random.randint(1,20)

for i in range(6):
    guessedNumber=int(input('Take a guess'))
    chanceTaken += 1

    if guessedNumber < randomNumber:
        print('Your guess is too low.')
    elif guessedNumber > randomNumber:
        print('Your guess is too high.')
    else:
        break

if guessedNumber==randomNumber:
    chanceTaken=str(chanceTaken)
    print('Good job, '+userName+'. You guessed my number in ' + chanceTaken+' guesses.')
else:
    randomNumber=str(randomNumber)
    print('Nope. The number I was thinking of was '+randomNumber+'.')
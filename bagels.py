import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNum():
    # Returns a string of unique random digits that is NUM_DIGITS long.
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    # Returns a string with the Pico, Fermi, & Bagels clues to the user.
    if guess == secretNum:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'

    clues.sort()
    return ' '.join(clues)

def isOnlyDigits(num):
    # Returns True if num is a string of only digits. Otherwise, returns False.
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True

print('I am thinking of a %s-digit number. Try to guess what it is.' %(NUM_DIGITS))
print('The clues I give are...')
print('When I say:  That means:')
print(' Bagles  None of the digits is correct.')
print(' Pico    One digit is correct but in the wrong position.')
print(' Fermi   One digit is correct and in the right position.')

while True:
    secretNum = getSecretNum()
    print('I have thought up a number. You have %s guesses to get it.' %(MAX_GUESS))
    
    guessesTaken = 1
    while guessesTaken <= MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGITS or isOnlyDigits(guess):
            print('Guess #%s: ' %(guessesTaken))
            guess = input()

            print(getClues(guess, secretNum))
            guessesTaken += 1

            if guess == secretNum:
                break
            if guessesTaken > MAX_GUESS:
                print('You rna out of guesses. The answer was %s.' %(secretNum))

        print('Do you want to play again? (yes or no)')
        if not input().lower().startswith('y'):
            break





# my code
'''
def printIntro():
    print("I am thinking of a 3-digit number. Try to guess what it is")
    print("The clues I give are...")
    print("when I say:\tThat means:")
    print("    Bagels\tNone of the digits is correct.")
    print("    Pico\tOne digit is correct but in the wrong position.")
    print("    Fermi\tOne digit is correct in the right position.")

def getRandomNumber():
    numbers= list(range(10))
    random.shuffle(numbers)
    randomString=''
    for i in range(3):
        randomString += str(numbers[i])
    print("I have thought up a number. You have 10 guesses to get it.")
    return randomString

def isItThere(guess, rightAnswer):
    for i in range(len(rightAnswer)):
        if guess == rightAnswer[i]:
            return True
    return False


printIntro()
playAgain = True

while(playAgain):
    randomNumber=getRandomNumber()

    for i in range(1,11):
        print("Guess #",i)
        guessedNumber = input()
        if randomNumber == guessedNumber:
            print('You got it!')
            break
        else:
            for i in range(3):
                if isItThere(guessedNumber[i],randomNumber) and guessedNumber[i]==randomNumber[i]:
                    print('Fermi ',end='')
                elif isItThere(guessedNumber[i],randomNumber) and guessedNumber[i]!=randomNumber[i]:
                    print('Pico ',end='')
        print('\n')
    
    print('The answer is',randomNumber)
    print('\nDo you want to play again? (yes or no)')
    playAgain=input().lower().startswith('y')
    '''
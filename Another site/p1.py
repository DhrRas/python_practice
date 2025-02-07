'''Bagels game
'''


import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
  while True:
    secretNum = getSecretNum()
    print('I have thought up a number.')
    print('You have {} guesses to get it.'.format(MAX_GUESSES))

    numGuesses = 1
    while numGuesses <= MAX_GUESSES:
      guess = ''
      while len(guess) != NUM_DIGITS or not guess.isdecimal():
        print("Guess #{}: ".format(numGuesses))
        guess = input('> ')

      clues = getClues(guess, secretNum)
      print(clues)
      numGuesses += 1

      if guess == secretNum:
        break
      if numGuesses > MAX_GUESSES:
        print('You ran out of guesses.')
        print('The answer was {}.'.format(secretNum))


    print('Do you want to play again? (yes or no)')
    if not input('> ').lower().startswith('y'):
      break

  print('Thanks for playing!')

def getSecretNum():
  '''Returns a string made up of num_digits unique random digits.'''
  numbers = list('0123456789')
  random.shuffle(numbers)

  secretNum = ''
  for i in range(NUM_DIGITS):
    secretNum += str(numbers[i])
    

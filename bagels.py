
Open In Colab

#BAGELLLSSSS


import random

digits, guesses = 3,10

def main():
  print('''Bagels, a deductive logic game.

  
  I am thinking of a {}-digit number with no repeated digits.
  Try to guess what it is. Here are some clues:
  When I say:    That means:
    Pico         One digit is correct but in the wrong position.
    Fermi        One digit is correct and in the right position.
    Bagels       No digit is correct.
 
  For example, if the secret number was 248 and your guess was 843, the
  clues would be Fermi Pico.'''.format(digits))

  while True:
    secretnum = getSecretNum()
    print("I have a number")
    print(' You have {} guesses to get it.'.format(guesses))

    numguess = 1
    while numguess<=guesses:
      guess =''
      while len(guess)!=digits or not guess.isdecimal():
        print('Guess #{}:'.format(numguess))
        guess = input('> ')

      clues = getClues(guess,secretnum)

      print(clues)
      numguess+=1
      
      if guess == secretnum:
        break
      if numguess>guesses:
        print('no guesses remaining')

        print('The answer was {}.' .format(secretnum))
      
    print('Do you want to play again? (yes or no)')
    if not input('> ').lower().startswith('y'):
      break
  print('Thanks for playing!') 




def getSecretNum():
  numbers = list('0123456789')
  random.shuffle(numbers)
  secretnum=''
  for i in range(digits):
    secretnum+=str(numbers[i])
  return secretnum


def getClues(guess, secretNum):
  if guess == secretNum:
    return 'You got it!'

  clues = []

  for i in range(len(guess)):
      if guess[i] == secretNum[i]:
          # A correct digit is in the correct place.
          clues.append('Fermi')
      elif guess[i] in secretNum:
          # A correct digit is in the incorrect place.
          clues.append('Pico')
  if len(clues) == 0:
      return 'Bagels'  # There are no correct digits at all.
  else:
      # Sort the clues into alphabetical order so their original order
      # doesn't give information away.
      clues.sort()
      # Make a single string from the list of string clues.
      return ' '.join(clues)


if __name__ == '__main__':
  main()

     

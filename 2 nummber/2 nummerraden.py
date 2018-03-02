import random

print('=======================================================')
print('                GUESS THAT NUMBER GAME')
print('=======================================================')
print('')

min_number = 0
max_number = 100
the_number = random.randint(min_number, max_number)
#print(the_number)
guess_int = -1

while guess_int != the_number:
    guess_text = input('Guess a number between {} and {}: '.format(min_number, max_number))
    guess_int = int(guess_text)

    if guess_int < the_number:
        print('your guess of {} was too low'.format(guess_int))
    elif guess_int > the_number:
        print('your guess of {} was too high'.format(guess_int))
    else:
        print('you win! the number was {}'.format(the_number))
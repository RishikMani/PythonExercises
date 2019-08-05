import numpy as np
import numbers

min_num = 0
max_num = 50

print('This program will generate random integers between 0 and 50. Guess it ;)')

def random_num_generator():
    random_num = np.random.randint(min_num, max_num + 1)
    return random_num
    
def want_to_continue():
    reply = input("Do you want to continue? Press Y for yes or N for no!")
    if type(reply) is not str:
        print('Please type in only Y or N.')
        return True
    elif reply.lower() not in ('y', 'n'):
        print('Please type in only Y or N.')
        return True
    else:
        if reply.lower() == 'y': True
        else: False

random_num = random_num_generator()
print('A random number has been generated. Guess the number, if you can ;)')

while True:    
    guess_num = input('Enter a number: ')
    if not isInstance(guess_num, numbers.Integral):
        print('Please type in an integer value only')
    else:
        if guess_num > random_num:
            print('You provided a wrong number. It is too big. Please guess a new number.')
        elif guess_num < random_num:
            print('You provided a wrong number. It is too small. Please guess a new number.')
        elif random_num == guess_num:
            print('Boom. You got it mate. Great!')
    
    _continue = want_to_continue()
    if _continue: continue
    else: break
    
print('The program has ended. Come back again, please... :(')

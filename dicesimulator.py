import numpy as np

print('This is a dice rolling simulator programme.')

'''number of times the dice would be thrown'''
num_throws = 10

for turn in range(num_throws):
    '''generate a random number between 1 and 6, inclusive both numbers'''
    number = np.random.randint(1,7)
    print('The number %d showed on dice throw' %number)

print('Exiting dice simulator program...')

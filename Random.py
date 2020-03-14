from random import choice
from random import sample
import pygame

pygame.time.wait(2000)
person_Weight_set = {
    "Kelly": 42,
    "Jhon": 28,
    "Thalia": 60,
    }
key = choice(list(person_Weight_set))
print(key+", weight", person_Weight_set[key], 'pounds, you have been selected to test our new challenge run!')
pygame.time.wait(5000)
print('Now, what to do with that baby over there...')
pygame.time.wait(3000)
print('Exiting Program')
for i in range(5):
    pygame.time.wait(900)
    print('.')
    pygame.time.wait(500)
    print('..')
    pygame.time.wait(500)
    print('...')

print('Quit successful!')
pygame.time.wait(1000)

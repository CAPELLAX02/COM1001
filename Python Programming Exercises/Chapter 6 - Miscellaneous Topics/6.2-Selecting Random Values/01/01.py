# The following program demonstrates functions from the 'random' module.

import random

elements = ['earth', 'air', 'fire', 'water', 'rock', 'dirt']

print(random.choice(elements))
# water

print(random.sample(elements, 2))
# ['fire', 'earth']

random.shuffle(elements)
print(elements)
# ['fire', 'dirt', 'water', 'rock', 'earth', 'air']

print(random.randint(1, 5))
# 5

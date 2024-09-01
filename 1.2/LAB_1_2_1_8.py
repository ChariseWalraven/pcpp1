import random

class Apple:
    counter = 0
    total_weight = 0

    def __init__(self):
        self.weight = random.uniform(0.2, 0.5)
        Apple.counter += 1
        Apple.total_weight += self.weight


apples = []

# limiting weight to 300 results in a final weight that almost always exceeds 300 by a couple of tenths
while Apple.counter < 1000 and Apple.total_weight < 299.8:
    apples.append(Apple())
else:
    print(f'processed {Apple.counter} apples, for a total weight of {Apple.total_weight} units')

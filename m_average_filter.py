import matplotlib.pyplot as plt
import math as m
import numpy as np
import random

#a = [50 * m.sin(5*2 * m.pi * i / 1000)+random.randint(-5, 5) for i in range(1000)]
a = [0 for i in range(1000)]
a[500] = 50

weights = [0 for i in range(201)]
amp = 0.5
for i in range(0, int(len(weights) / 2) + 1):
    weights[int(len(weights)/2)+i] = amp*m.cos(2*m.pi*i/len(weights))+amp
    weights[int(len(weights)/2)-i] = amp*m.cos(2*m.pi*i/len(weights))+amp
print(sum(weights))


def filter(input, weights):
    output = [0 for i in range(len(input)-len(weights))]

    offset = 0
    for outputIndex in range(len(output)):
        sum = 0
        for weightIndex in range(len(weights)):
            sum += weights[weightIndex] * input[offset + weightIndex]
        offset += 1
        output[outputIndex] = sum

    return output


plt.plot(filter(a, weights))
plt.show()

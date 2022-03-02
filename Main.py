from Neuron import Neuron
import random


p1 = Neuron("AND-gate")
p1.b = random.uniform(-1, 1)
p1.w = [random.uniform(-1, 1), random.uniform(-1, 1)]

p2 = Neuron("OR-gate")
p2.b = random.uniform(-1, 1)
p2.w = [random.uniform(-1, 1), random.uniform(-1, 1)]

# print("AND-gate")
# p1.update([[0, [0, 0]], [0, [0, 1]], [0, [1, 0]],  [1, [1, 1]]], 30)
# print("OR-gate")
# p2.update([[0, [0, 0]], [1, [0, 1]], [1, [1, 0]], [1, [1, 1]]], 30)


p1.activate([0, 0])
print(p1)

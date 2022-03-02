from __future__ import print_function


class Neuron:
    def __init__(self, name, w=None):
        self.name = name
        self.b = 0
        self.e = 2.718281828459045
        self.msg = -1
        if w is None:
            w = []
        self.w = w

    def __str__(self):
        return self.msg

    def update(self, truthtable, epochs=25, show=False):
        for i in range(epochs):
            for row in truthtable:
                d = row[0]
                x = row[1]
                y = self.activate(x)  # output

                self.msg +="    t:   " + str(d)
                if show:
                    print(self)
                elif i + 1 == epochs:
                    print(self)

                e = d - y
                for j in range(len(self.w)):
                    self.w[j] += 0.2 * e * x[j]
                self.b += 0.2 * e

    def activate(self, event):
        self.msg = ""
        som = 0
        for i in range(len(self.w)):
            self.msg += "'" + str(event[i]) + "i " + str(self.w[i]) + "w" + "'  "
            som = som + event[i]*self.w[i]
        self.msg += str(self.b) + "b  "
        sigmoid_function = 1 / (1 + self.e**-(som + self.b))
        return sigmoid_function


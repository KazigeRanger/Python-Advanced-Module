import numpy as np
import matplotlib.pyplot as plt

class Neuron :
    # Dezelfde code als hierboven
    def __init__(self):
        # Willekeurige getallen tussen -0.5 en 0.5 (gebruik eventueel random van numpy)
        self.W = np.array(np.random.rand(2))
        self.B = 0

    def forward(self, X):
    # Bereken hier de gewogen som Z (=dot-product van self.W en X) met numpy.dot
        self.Z = np.dot(self.W, X)+self.B
    # de output slaan we op in de variabele self.A
        self.A = 0
        if( self.Z > 0 ) : self.A = 1
        return self.A

# Create n random 2D (x1,x2) training data
n = 1000
#np.random.seed(1) # uncomment to get reproducible results
x = np.random.rand(n,2)

# Pick random numbers for the true weights and true bias
weights = np.random.random(2)*0.5 + 0.5
bias = -np.random.random()*0.25 - 0.5

# get the true y values
y = np.zeros(n)
for i in range(n) :
    if np.dot(weights, x[i]) + bias > 0 : y[i] = 1

# Maak een netwerk met een enkel neuron
network = Neuron()

# Vals spelen: we vertellen het netwerk stiekem wat de goede waarden moeten zijn
network.W = weights
network.B = bias

# Plot het resultaat van het perceptron als een lijn (grens tussen 0 en 1)
x1line = np.array([0,1]) # we rekenen twee punten uit voor x=0 en x=1
# vul hier jouw code in:
x2line = -(network.W[0]/network.W[1])*x1line-(network.B/network.W[1])

# Plot the data points
plt.figure()
plt.ylim(0, 1.0)
plt.gca().set_xlabel("x1", loc='right',fontsize=14)
plt.gca().set_ylabel("x2", loc='top', fontsize=14)
# Plot the data points on top
plt.scatter(x[:,0], x[:,1],c=y, cmap="PuOr",edgecolors='white', linewidth=0.5)
plt.plot(x1line, x2line, color='red', linewidth=3)
plt.show(block=False)

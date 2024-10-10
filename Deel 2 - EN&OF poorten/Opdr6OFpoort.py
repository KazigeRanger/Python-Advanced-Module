import numpy as np

class Neuron :
    def __init__(self):
        # Willekeurige getallen tussen -0.5 en 0.5 (gebruik eventueel random van numpy)
        self.W = np.array(np.random.rand(2))

    def forward(self, X):
    # Bereken hier de gewogen som Z (=dot-product van self.W en X) met numpy.dot
        self.Z = np.dot(self.W, X)
    # de output slaan we op in de variabele self.A
        self.A = 0
        if( self.Z > 0 ) : self.A = 1
        return self.A

# Test inputs: alle vier de mogelijke invoercombinaties van 2 inputs 
x = np.array([[0, 0], [1,0], [0,1],[1,1]])

# Maak een netwerk met een enkel neuron
network = Neuron()

# Voer een forward-propagatie uit
print("Met random gewichten:", network.W)
for i in range(4) :
    output = network.forward( x[i] )
    print("Input = ", x[i], ", Netwerk output ", output)

# Kies een set van juiste gewichten (vervang dus de initiele waarden)
network.W = np.array([0.5, 0.5]) # vul hier jouw getallen in
print("Met deze gewichten:", network.W)
for i in range(4) :
    output = network.forward( x[i] )
    print("Input = ", x[i], ", Netwerk output ", output)
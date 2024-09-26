import numpy as np

# aantallen van elk type fruit voor 5 verschillende personen
aantallen_fruit = np.array([
    [4, 2, 5, 3],
    [3, 1, 4, 0],
    [2, 5, 1, 2],
    [1, 4, 3, 1],
    [5, 0, 2, 4]
])

# prijzen per stuk voor elk type fruit
prijzen_per_stuk = np.array([0.5, 0.3, 0.7, 1.2])

# functie die de berekening kan uitvoeren
def bereken_totaalprijs(aantallen, prijzen):
    for i in range(len(aantallen)):
        print(str(aantallen[i]) + " * " + str(prijzen) + " = " + str(np.dot(aantallen[i], prijzen)))
    
    print("Matrix dot product is: " + str(np.dot(aantallen, prijzen)))
    print("Output array element 4: " + str(np.dot(aantallen, prijzen)[3]))
    return np.dot(aantallen, prijzen)

totaalprijs_per_persoon = bereken_totaalprijs(aantallen_fruit, prijzen_per_stuk)
print(totaalprijs_per_persoon)
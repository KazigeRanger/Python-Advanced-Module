import numpy as np

# aantallen van elk type fruit in het mandje
aantallen_fruit = [4, 2, 5, 3]

# prijzen per stuk voor elk type fruit
prijzen_per_stuk = [0.5, 0.3, 0.7, 1.2]

# Functie om de totale prijs van het mandje te berekenen
def bereken_totaalprijs(aantallen, prijzen):
    return np.dot(aantallen, prijzen)

totaalprijs = bereken_totaalprijs(aantallen_fruit, prijzen_per_stuk)
print(totaalprijs)
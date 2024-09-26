import numpy as np

# 8 random inputs (bijv. kenmerken van een stuk fruit)
inputs = np.random.rand(8)

# 8 random gewichten
gewichten = np.random.rand(8)

# Jouw taak: Maak een functie om de gewogen som te berekenen
def bereken_gewogen_som(inputs, gewichten):
    return np.dot(inputs, gewichten)

gewogen_som = bereken_gewogen_som(inputs, gewichten)
print(gewogen_som)
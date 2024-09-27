# Dit programma is alleen bedoeld om te oefenen met fitnessfuncties en ermee te experimenteren
# Dus het neurale netwerk zelf is zeer onnauwkeurig, maar het was ook niet de bedoeling om een 
# nauwkeurig neuraal netwerk te programmeren in dit programma.
import numpy as np

# Definieer de input
input_sentence = input("Typ een simpele zin in de tegenwoordige of verleden tijd: ")

weights = np.random.rand(10)
print(str(weights))

activation_multiplier = 0.43226820450000003

def evaluate_sentence(input_sentence, weights):
    input_value = len(input_sentence)
    print(str(np.dot(input_value, weights)))
    print(str(np.sum(np.dot(input_value, weights))))
    output_value = np.sum(np.dot(input_value, weights))/len(weights)

    activation_value = activation_multiplier*len(input_sentence)

    print(f"Activation value: {activation_value} \nOutput Value: {output_value}")

    if output_value > activation_value:
        print("De zin staat in de tegenwoordige tijd.")
        return
    elif output_value < activation_value:
        print("De zin staat in de verleden tijd.")
        return
    
model_evaluation = evaluate_sentence(input_sentence, weights)

def fitnessFunction(correct_evaluation):
    print("Bedankt voor de feedback. Het model wordt geupdatet.")

    with open(__file__, 'r') as file:
        lines = file.readlines()

    with open(__file__, 'w') as file:
        for line in lines:
            if line.startswith("activation_multiplier =") and correct_evaluation == "tegenwoordige tijd":
                file.write(f"activation_multiplier = {activation_multiplier-activation_multiplier/10}\n")
            elif line.startswith("activation_multiplier =") and correct_evaluation == "verleden tijd":
                file.write(f"activation_multiplier = {activation_multiplier+activation_multiplier/10}\n")
            else:
                file.write(line)



user_evaluation = input("Is de evaluatie correct? Typ \"ja\" of \"nee\": ")
if user_evaluation == "ja":
    print("Bedankt voor de feedback.")
elif user_evaluation == "nee":
    correct_evaluation = input("In welke tijd stond de zin die je als input hebt gegeven? Typ \"verleden tijd\" of \"tegenwoordige tijd\": ")
    fitnessFunction(correct_evaluation)
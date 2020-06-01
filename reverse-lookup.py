dictionary = {"burger": 1, "fries": 1, "pizza": 2, "hot dog": 4, "chicken nuggets": 5, "fries": 5, "coke": 5}

input_value = int(input("Try your luck, type a number from 1-5 and see what food you'll get: "))

output_keys = []

def function (dictionary, input_value):
    for key, value in dictionary.items():
        if (value == input_value):
            output_keys.append(key)
    print(output_keys)

function(dictionary, input_value)
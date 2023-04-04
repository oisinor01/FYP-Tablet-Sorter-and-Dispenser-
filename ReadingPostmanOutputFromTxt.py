import json

# open txt file in read mode
with open(r'C:\Users\orour\Scripts\probability.txt', 'r') as p:
    data = p.read()

# Parse the JSON data into a Python object
data_dict = json.loads(data)

# Find the prediction with the highest probability and print its tagName
max_prediction = max(data_dict['predictions'], key=lambda x: x['probability'])
print(max_prediction['tagName'])

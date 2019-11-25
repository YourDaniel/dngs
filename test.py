import pandas as pd
df = pd.read_csv('resources_material.csv')
import json
with open('data.json', 'r', encoding='UTF-8-sig') as file:
    data = json.load(file)

print(data[0]['material'])
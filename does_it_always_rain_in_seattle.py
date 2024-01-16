import json

with open ('precipitation.json', encoding= 'utf-8') as file:
    precipitation = json.load(file)

seattle_results = []
for measurement in precipitation:
    city = measurement['station']
    if city == 'GHCND:US1WAKG0038':
        seattle_results.append(measurement)


print(seattle_results)

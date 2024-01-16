import json
with open ('precipitation.json', encoding= 'utf-8') as file:
    precipitation = json.load(file)

# Selecting Seattle out of the precipitation.json file and splitting the dates (to extract the month later on):
    
seattle_results = []
for measurement in precipitation:
    city = measurement['station']
    if city == 'GHCND:US1WAKG0038':
        seattle_results.append(measurement)
    measurement['date'] = measurement['date'].split('-')

# Calculating the total monthly precipitation:
    
total_monthly_precipitation = {} 
for month in seattle_results:
    if month['date'][1] in total_monthly_precipitation:
        total_monthly_precipitation[month['date'][1]] = total_monthly_precipitation[month['date'][1]] + month['value']
    else:
        total_monthly_precipitation[month['date'][1]] = month['value']

total_monthly_precipitation_list = []
for key, value in total_monthly_precipitation.items():
    total_monthly_precipitation_list.append(value)

# Saving the results to a result file:
    
results = {
    'Seattle': {
        'station': 'GHCND:US1WAKG0038',
        'state': 'WA',
        'total_monthly_precipitation': total_monthly_precipitation_list
    }
}

with open ('results.json', 'w', encoding = 'utf-8') as file:
    json.dump(results, file, indent = 3)

print(results)

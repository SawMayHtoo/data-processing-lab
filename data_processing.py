import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()



# # Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
print("All city in Germany")
for city in cities:
    if city["country"] == "Germany":
        print(city["city"])

print()
# Print all cities in Spain with a temperature above 12°C

print("All cities in Spain with a temperature above 12°C:")
for city in cities:
    if city["country"] == "Spain" and float(city["temperature"]) > 12:
        print(city["city"])

print()
# Count the number of unique countries

unique_countries = set()
for x in cities:
    unique_countries.add(x["country"])
print(f"Number of unique countries {len(unique_countries)}")

print()

# Print the average temperature for all the cities in Germany
Germany_temperture = []
for x in cities:
    if x["country"] == "Germany":
        Germany_temperture.append(float(x["temperature"]))

average_temperature = sum(Germany_temperture)/ len(Germany_temperture)
print("The average temperature for all cities in Germany:" ,average_temperature)
print()

# Print the max temperature for all the cities in Italy
italy_temp = []
for x in cities:
    if x['country'] == "Italy":
        italy_temp.append(float(x["temperature"]))

print("Max temperature in all cities of Italy:", max(italy_temp))
print()

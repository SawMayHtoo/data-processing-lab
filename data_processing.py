import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))


def filter_items(condition, dict_list):
    filtered = []
    for item in dict_list:
        if condition(item):
            filtered.append(item)
    return filtered


def aggregate(aggregation_key, aggregation_function, dict_list):
    values = []
    for item in dict_list:
        try:
            values.append(float(item[aggregation_key]))
        except ValueError:
            values.append(item[aggregation_key])
    return aggregation_function(values)


# 1. Print the average temperature of all the cities
print("The average temperature of all the cities:")
print(aggregate("temperature", lambda x: sum(x) / len(x), cities))
print()

# 2. Print all cities in Germany
print("All cities in Germany:")
german_cities = filter_items(lambda c: c["country"] == "Germany", cities)
print([c["city"] for c in german_cities])
print()

# 3. Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temperature above 12°C:")
warm_spain = filter_items(lambda c: c["country"] == "Spain" and float(c["temperature"]) > 12, cities)
print([c["city"] for c in warm_spain])
print()

# 4. Count the number of unique countries
print("The number of unique countries:")
print(aggregate("country", lambda x: len(set(x)), cities))
print()

# 5. Print the average temperature for all the cities in Germany
print("The average temperature for all the cities in Germany:")
print(aggregate("temperature", lambda x: sum(x) / len(x), german_cities))
print()

# 6. Print the max temperature for all the cities in Italy
print("The max temperature for all the cities in Italy:")
italian_cities = filter_items(lambda c: c["country"] == "Italy", cities)
print(aggregate("temperature", max, italian_cities))
print()
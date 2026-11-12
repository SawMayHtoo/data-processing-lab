import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


class DataLoader:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        data = []
        with open(os.path.join(__location__, self.filename)) as f:
            rows = csv.DictReader(f)
            for r in rows:
                data.append(dict(r))
        return Table(self.filename, data)


class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def filter(self, condition):
        filtered = []
        for item in self.table:
            if condition(item):
                filtered.append(item)
        return Table(self.table_name + "_filtered", filtered)

    def aggregate(self, aggregation_key, aggregation_function):
        values = []
        for item in self.table:
            try:
                values.append(float(item[aggregation_key]))
            except ValueError:
                values.append(item[aggregation_key])
        return aggregation_function(values)

    def __str__(self):
        return self.table_name + ":" + str(self.table)


# Load Cities.csv into a Table object
cities_table = DataLoader('Cities.csv').load()

# 1. Print the average temperature of all the cities
print("The average temperature of all the cities:")
print(cities_table.aggregate("temperature", lambda x: sum(x) / len(x)))
print()

# 2. Print all cities in Germany
print("All cities in Germany:")
german_cities = cities_table.filter(lambda c: c["country"] == "Germany")
print([c["city"] for c in german_cities.table])
print()

# 3. Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temperature above 12°C:")
warm_spain = cities_table.filter(lambda c: c["country"] == "Spain" and float(c["temperature"]) > 12)
print([c["city"] for c in warm_spain.table])
print()

# 4. Count the number of unique countries
print("The number of unique countries:")
print(cities_table.aggregate("country", lambda x: len(set(x))))
print()

# 5. Print the average temperature for all the cities in Germany
print("The average temperature for all the cities in Germany:")
print(german_cities.aggregate("temperature", lambda x: sum(x) / len(x)))
print()

# 6. Print the max temperature for all the cities in Italy
print("The max temperature for all the cities in Italy:")
italian_cities = cities_table.filter(lambda c: c["country"] == "Italy")
print(italian_cities.aggregate("temperature", max))
print()
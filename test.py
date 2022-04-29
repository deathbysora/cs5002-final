import csv
from datetime import datetime
import os

path = os.getcwd() + "\\data\\2019_january.csv"
with open(path, "r") as file:
    reader = csv.reader(file)

    next(reader)
    days = {line[0].split()[0] for line in reader}

print(*days, sep="\n")
print()
result = [datetime.strptime(day, "%m/%d/%Y").day for day in days]
print(*result, sep="\n")

import csv
from pathlib import Path

PATH_CSV = Path(__file__).parent / "C:\\Users\\diham\\OneDrive\\Área de Trabalho\\corona.csv"
print(PATH_CSV)

# opção 1
with open(PATH_CSV, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)

# opção 2
with open(PATH_CSV, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for line in reader:
        print(line)

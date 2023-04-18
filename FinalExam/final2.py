import os.path
import csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
corn = os.path.join(BASE_DIR, "CornProduction2008-2018.csv")

county = input("Enter name of county (all upper-case): ").upper()
numList = []
avg = 0

with open(corn, newline='') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    # TODO: read the file's data, find rows matching the county, and compute the min, max, and avg bushels for the county
    for row in reader:
        if row[1] == county:
            numList.append(int(row[2]))          
    avg = sum(numList) / len(numList)
    
    print("County",county,"max corn production: ",max(numList))
    print("County",county,"avg corn production: ",avg)
    print("County",county,"max corn production: ",min(numList))
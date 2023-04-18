import csv

input_csv = input('Enter a csv file: ')

volumeByCounty = {}

with open(input_csv, newline='') as csvfile:
    Sales = csv.reader(csvfile)
    headers = next(Sales)
    sampleData = list(Sales)

    for county in sampleData:
        if county[9] != '':
            county[9] = county[9].upper()
            current_sales = volumeByCounty.get(county[9], 0.0)
            volumeByCounty[county[9]] = current_sales + float(county[22])

    print('Total County Alcohol Sales By Volume: ')
    index = 0
    liters = 0

    for county, volume in sorted(volumeByCounty.items(), key=lambda x: x[1], reverse=True):
        index += 1
        print('{:3}. {:15} {:15.2f}'.format(index, county,volumeByCounty[county]), 'liters')
        liters += volumeByCounty[county]

    liters = '{:.2f}'.format(liters)
    print('Total sales in Iowa: ', liters, 'liters')

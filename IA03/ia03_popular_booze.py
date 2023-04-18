import csv

input_csv = input("Enter a csv file: ")

volume_by_store = {}
with open('input_csv', newline= '') as csvfile:

    csvreader = csv.reader(csvfile)
    headers = next(csvreader)

    for row in csvreader:
        item_name = row[15]
        store_name = row[3]
        volume = float(row[22])
        county_name = row[9].upper()
        if county_name == "JOHNSON":
            if store_name not in volume_by_store:
                volume_by_store[store_name] = {}
            if item_name not in volume_by_store[store_name]:
                volume_by_store[store_name][item_name] = 0.0
            volume_by_store[store_name][item_name] += volume
    
    print("Most popular product by volume in each store in JOHNSON county:")
    index = 0
    for store_name in volume_by_store:
        for item_name, volume in sorted(volume_by_store[store_name].items(), key=lambda x: x[1], reverse=True):
            index += 1
            print('{:3}. {} {} {:15.2f} {}'.format(index, store_name, item_name, volume, 'liters'))
            break
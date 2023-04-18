import csv
data = [] 
with open('sample.csv','r') as csvFile: #C:\MIS407\mis407s21-student-15\sample.csv was used in testing

    reader = csv.reader(csvFile)
    headers = next(reader)
    data.append(headers)

    for row in reader:
        if(len(row)>=7):
            if(row[6]=='IL'):
                data.append(row)
print(data)

if(len(data)>=1):
    with open('illnois.csv','a',newline='') as csvFile:
        writer = csv.writer(csvFile)
        for row in data:
            writer.writerow(row)
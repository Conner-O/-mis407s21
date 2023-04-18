import csv
openCSV = open('sample.csv') #C:\MIS407\mis407s21-student-15\sample.csv was used in testing
reader = csv.reader(openCSV)
data = []
for row in reader:
        data.append(row)

openCSV.close()
  
for row in data:
        print(row)

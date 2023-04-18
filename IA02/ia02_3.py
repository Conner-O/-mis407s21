import csv
countMN = 0 
countMO = 0 

with open('sample.csv','r') as csvFile: #C:\MIS407\mis407s21-student-15\sample.csv was used in testing
    reader = csv.reader(csvFile)
    headers = next(reader)

    for row in reader:
        if(row[7]=='MN'):
            countMN+=1
        elif(row[6]=='MO'):
            countMO+=1

print('MN: total = {}'.format(countMN))
print('MO: total = {}'.format(countMO))
# ICA06 - Query the booze.sqlite file for stores in a given county
# booze.sqlite: volumes by store for Polk county
# Columns:
# (ID 'INTEGER' PRIMARY KEY AUTOINCREMENT, STORE_NAME 'TEXT', PRODUCT_NAME 'TEXT', VOLUME 'REAL')
import sqlite3
sqlite_file = 'booze.sqlite'
table_name = 'booze'
store = input("Enter store name to search: ")
store = '%' + store + '%'
conn = sqlite3.connect(sqlite_file)
cur = conn.cursor()
# TODO: Select rows from the table by store name ordered by volume.
cur.execute("SELECT * FROM {tn} WHERE STORE_NAME LIKE ? ORDER BY VOLUME DESC" .format(tn=table_name), (store,))

print("Matches for store {}".format(store))
number = 0
total = 0.0
for row in cur:
    number += 1
    total += row[3]
    print("{:3d}. {:20s} {:20s} {:10,.2f} liters".format(number, row[1], row[2], row[3]))
print("Total volume sold at stores matching {}: {}".format(store, total))

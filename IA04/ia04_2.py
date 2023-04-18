
import sqlite3
import os.path
#sqlite_file = "booze-polk.sqlite"
table_name = "booze"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "booze-polk.sqlite")

product = input("Enter product name to search: ")
product = '%' + product + '%'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("SELECT STORE_NAME, PRODUCT_NAME, SUM(VOLUME) FROM {tn} WHERE PRODUCT_NAME LIKE ? GROUP BY STORE_NAME, PRODUCT_NAME ORDER BY STORE_NAME, PRODUCT_NAME" .format(tn=table_name), (product,))



print("Matches for product {}".format(product))
number = 0
total = 0.0
for row in cur:
    number += 1
    total += row[2]
    print("{:3d}. {} {} {} liters".format(number, row[0],row[1], row[2],))
print("Total volume sold at stores matching {}: {}".format(product, total))

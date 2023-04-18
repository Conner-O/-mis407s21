import sqlite3

# Columns: ['id', 'first_name','last_name','hours','pay_rate']
rows = [
    [1,"James","Hansen",22,16.25],
    [2,"Josephine","Darakjy",32,15.55],
    [3,"Art","Venere",35,14.44],
    [4,"Lenna","Paprocki",35,18.90],
    [5,"Donette","Foller",28,18.90],
    [6,"Simona","Morasca",30,17.50],
    [7,"Mitsue","Tollner",30,19.22],
    [8,"Leota","Dilliard",30,18.90],
    [9,"Sage","Wieser",32,16.25],
    [10,"Kris","Marrier",32,21.10],
    [11,"Minna","Amigon",32,20.50],
    [12,"Ryan","O'Reilly",25,15.55]
]

sqlite_filename = input("Enter name of the SQLite file to use: ")
conn = sqlite3.connect(sqlite_filename)
c = conn.cursor()
# Run the CREATE TABLE statement for the columns named in the header.
create_table_stmt = "CREATE TABLE IF NOT EXISTS employee (id INTEGER, first_name TEXT, last_name TEXT, hours REAL, pay_rate REAL)"
c.execute(create_table_stmt)
# Cleanup any pre-existing data from prior runs of the program
c.execute("DELETE FROM employee")
conn.commit()

for row in rows:
    # TODO: Insert each employee's data into the employee SQL table.
    sql_insert="insert into employee values(?,?,?,?,?)"
    c.execute(sql_insert,row)
    pass
conn.commit()

c.execute('SELECT first_name, last_name, hours, pay_rate, hours * pay_rate AS pay FROM employee ORDER BY last_name, first_name')
total_pay = 0.0
for row in c:
    # TODO: Print the row, and add the employee's pay to total_pay
    print(row)
    pay_rate = row[4]
    total_pay = total_pay + pay_rate
    pass
print("Total pay: {}".format(total_pay))
conn.close()

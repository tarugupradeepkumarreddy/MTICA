import sqlite3 as lite
con=lite.connect('pradeep.db')
cur=con.cursor()
cur.execute('''DROP TABLE IF EXISTS CARS''')
cur.execute('''CREATE TABLE  cars( Id INT,Name TEXT,Price INT)''')
print("table cars created.")
cur.execute("INSERT INTO cars VALUES(1,'Audi',561374)")
cur.execute("INSERT INTO cars VALUES(2,'Mercedes',789465)")
cur.execute("INSERT INTO cars VALUES(3,'Skoda',15986)")
cur.execute("INSERT INTO cars VALUES(4,'Volvo',753159)")
cur.execute("INSERT INTO cars VALUES(5,'Bentley',12503)")
cur.execute("INSERT INTO cars VALUES(6,'Citrorn',423657)")
cur.execute("INSERT INTO cars VALUES(7,'Hummber',75293)")
cur.execute("INSERT INTO cars VALUES(8,'Volkswagen',1583)")
con.commit()
print("values in table car inserted.")



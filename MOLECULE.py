import sqlite3

conn = sqlite3.connect('RAMAN.db')

c = conn.cursor()

c.execute("CREATE table MOLECULE (COMPUND NUMBER INT, COMPOUND NAME TEXT, \"COMPOUND FORMULA\" TEXT)");

c.execute("INSERT INTO MOLECULE VALUES (1, 'WATER', 'H20')");

c.execute("INSERT INTO MOLECULE VALUES (2, 'CARBON DI OXIDE', 'CO2')");

c.execute("INSERT INTO MOLECULE VALUES (3, 'SODIUM CLORIDE', 'NaCl')");

c.execute("INSERT INTO MOLECULE VALUES (4, 'BORON CARBIDE', 'BC')");

c.execute("INSERT INTO MOLECULE VALUES (5, 'ALUMINIUM OXIDE', 'AL2O3')");

c.execute("SELECT * FROM MOLECULE")

#rows = c.fetchall()

#for row in rows:
    #print row

#conn.commit()

#conn.close()

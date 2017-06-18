import sqlite3

conn = sqlite3.connect('RAMAN.db')

c = conn.cursor()

c.execute("CREATE table MOLECULE (MOL_NUMBER INT, MOL_NAME TEXT, \"MOL_FORMULA\" TEXT )");

c.execute("INSERT INTO MOLECULE VALUES (1, 'WATER', 'H20')");

c.execute("INSERT INTO MOLECULE VALUES (2, 'CARBON DI OXIDE', 'CO2')");

c.execute("INSERT INTO MOLECULE VALUES (3, 'SODIUM CLORIDE', 'NaCl')");

c.execute("INSERT INTO MOLECULE VALUES (4, 'BORON CARBIDE', 'BC')");

c.execute("INSERT INTO MOLECULE VALUES (5, 'ALUMINIUM OXIDE', 'AL2O3')");

c.execute("INSERT INTO MOLECULE VALUES (6, 'HYDROGEN PROXIDE', 'H202')");

c.execute("INSERT INTO MOLECULE VALUES (7, 'GLUOCOSE', 'C6H1206')");
 
c.execute("INSERT INTO MOLECULE VALUES (8, 'SUCROSE', 'C12H22O11')");

c.execute("SELECT * FROM MOLECULE")

rows = c.fetchall()

for row in rows:
    print row

conn.commit()

conn.close()

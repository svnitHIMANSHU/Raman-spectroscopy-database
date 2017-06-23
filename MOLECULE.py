import sqlite3

conn = sqlite3.connect('RAMAN.db')

c = conn.cursor()

c.execute("CREATE table MOLECULE (MOL_NUMBER INT, MOL_NAME TEXT, \"MOL_FORMULA\" TEXT, \"FILE_NAME\" TEXT )");

c.execute("INSERT INTO MOLECULE VALUES (1, 'WATER', 'H20', 'Pr25%Al75%FeGeO_RTP_R12.asc')");

c.execute("INSERT INTO MOLECULE VALUES (2, 'CARBON DI OXIDE', 'CO2', 'Pr75%Al25%FeGeO_RTP_R1.asc')");

c.execute("INSERT INTO MOLECULE VALUES (3, 'SODIUM CLORIDE', 'NaCl', 'Pr50%Al50%FeGeO_RTP_R1.asc')");

c.execute("INSERT INTO MOLECULE VALUES (4, 'BORON CARBIDE', 'BC', 'Pr25%Al75%FeGeO_RTP_R1.asc')");

c.execute("INSERT INTO MOLECULE VALUES (5, 'ALUMINIUM OXIDE', 'AL2O3', 'PrAlGeO_RTP_R1.asc')");

c.execute("INSERT INTO MOLECULE VALUES (6, 'HYDROGEN PROXIDE', 'H202', 'PrFeGeO_RTP_R12.asc')");

c.execute("INSERT INTO MOLECULE VALUES (7, 'GLUOCOSE', 'C6H1206', 'PrFeGeO_RTP_R1.asc')");
 
c.execute("INSERT INTO MOLECULE VALUES (8, 'SUCROSE', 'C12H22O11', '600_1%_532e_Mo F1_80sec.asc')");

c.execute("SELECT * FROM MOLECULE")

rows = c.fetchall()

for row in rows:
    print row

conn.commit()

conn.close()

import sqlite3

conn = sqlite3.connect('RAMAN.db')

c = conn.cursor()

c.execute("CREATE table LINK(ID INT, ELEMENT_NUMBER INT,  MOL_NUMBER INT)");

c.execute("INSERT INTO LINK VALUES (1, 1, '1')");

c.execute("INSERT INTO LINK VALUES (2, '8', '1')");

c.execute("INSERT INTO LINK VALUES (3, 6, '2')");

c.execute("INSERT INTO LINK VALUES (4, 8, '2')");

c.execute("INSERT INTO LINK VALUES (5, 11, '3')");

c.execute("INSERT INTO LINK VALUES (6, 17, '3')");

c.execute("INSERT INTO LINK VALUES (7, '5', '4')");

c.execute("INSERT INTO LINK VALUES (8, 6, '4')");

c.execute("INSERT INTO LINK VALUES (9, 13, '5')");

c.execute("INSERT INTO LINK VALUES (10, 8, '5')");

c.execute("INSERT INTO LINK VALUES (11, 1, '6')");

c.execute("INSERT INTO LINK VALUES (12, '8', '6')");

c.execute("SELECT * FROM LINK")

rows = c.fetchall()

for row in rows:
    print row

conn.commit()

conn.close()

import sqlite3

conn = sqlite3.connect('RAMAN.db')

c = conn.cursor()

c.execute("CREATE table LINK(ID INT, ELEMENT_NUMBER INT,  MOL_NUMBER INT)");

c.execute("INSERT INTO LINK VALUES (1, 1, '1')");

c.execute("INSERT INTO LINK VALUES (2, 8, '1')");

c.execute("INSERT INTO LINK VALUES (3, 6, '2')");

c.execute("INSERT INTO LINK VALUES (4, 8, '2')");

c.execute("INSERT INTO LINK VALUES (5, 11, '3')");

c.execute("INSERT INTO LINK VALUES (6, 17, '3')");

c.execute("INSERT INTO LINK VALUES (7, 5, '4')");

c.execute("INSERT INTO LINK VALUES (8, 6, '4')");

c.execute("INSERT INTO LINK VALUES (9, 13, '5')");

c.execute("INSERT INTO LINK VALUES (10, 8, '5')");

c.execute("INSERT INTO LINK VALUES (11, 1, '6')");

c.execute("INSERT INTO LINK VALUES (12, 8, '6')");

c.execute("INSERT INTO LINK VALUES (13, 1, '7')");

c.execute("INSERT INTO LINK VALUES (14, 8, '7')");

c.execute("INSERT INTO LINK VALUES (15, 6, '7')");

c.execute("INSERT INTO LINK VALUES (16, 1, '8')");

c.execute("INSERT INTO LINK VALUES (17, 8, '8')");

c.execute("INSERT INTO LINK VALUES (18, 6, '8')");

c.execute("INSERT INTO LINK VALUES (19, 8, '9')");

c.execute("INSERT INTO LINK VALUES (20, 6, '9')");

c.execute("INSERT INTO LINK VALUES (21, 58, '10')");

c.execute("INSERT INTO LINK VALUES (22, 23, '10')");

c.execute("INSERT INTO LINK VALUES (23, 8, '10')");

c.execute("INSERT INTO LINK VALUES (24, 58, '11')");

c.execute("INSERT INTO LINK VALUES (25, 8, '11')");

c.execute("INSERT INTO LINK VALUES (26, 23, '11')");

c.execute("INSERT INTO LINK VALUES (27, 15, '12')");

c.execute("INSERT INTO LINK VALUES (28, 8, '12')");

c.execute("INSERT INTO LINK VALUES (29, 58, '12')");

c.execute("SELECT * FROM LINK")

rows = c.fetchall()

for row in rows:
    print row

conn.commit()

conn.close()

conn.close()

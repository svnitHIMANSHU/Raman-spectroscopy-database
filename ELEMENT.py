import sqlite3

conn = sqlite3.connect('RAMAN.db')

c = conn.cursor()

c.execute("CREATE table ELEMENT(ATOMIC_NUMBER INT, SYMBOL TEXT, ROW_NO INT,COLUMN_NO INT)");

c.execute("INSERT INTO ELEMENT VALUES (1, 'H', 1, '1')");

c.execute("INSERT INTO ELEMENT VALUES (2, 'He', 1, '18')");

c.execute("INSERT INTO ELEMENT VALUES (3, 'Li', 2, '1')");

c.execute("INSERT INTO ELEMENT VALUES (4, 'Be', 2, '2')");
      
c.execute("INSERT INTO ELEMENT VALUES (5, 'B', 2, '13')");
      
c.execute("INSERT INTO ELEMENT VALUES (6, 'C', 2, '14')");

c.execute("INSERT INTO ELEMENT VALUES (7, 'N', 2, '15')");

c.execute("INSERT INTO ELEMENT VALUES (8, 'O', 2, '16')");

c.execute("INSERT INTO ELEMENT VALUES (9, 'F', 2, '17')");
 
c.execute("INSERT INTO ELEMENT VALUES (10, 'Ne', 2, '18')");

c.execute("INSERT INTO ELEMENT VALUES (11, 'Na', 3, '1')");

c.execute("INSERT INTO ELEMENT VALUES (12, 'Mg', 3, '2')");
      
c.execute("INSERT INTO ELEMENT VALUES (13, 'Al', 3, '13')");
      
c.execute("INSERT INTO ELEMENT VALUES (14, 'Si', 3, '14')");

c.execute("INSERT INTO ELEMENT VALUES (15, 'P', 3, '15')");

c.execute("INSERT INTO ELEMENT VALUES (16, 'S', 3, '16')");

c.execute("INSERT INTO ELEMENT VALUES (17, 'Cl', 3, '17')")

c.execute("INSERT INTO ELEMENT VALUES (18, 'Ar', 3, '18')");
      
c.execute("INSERT INTO ELEMENT VALUES (19, 'K', 4, '1')");

c.execute("INSERT INTO ELEMENT VALUES (20, 'Ca', 4, '2')");

c.execute("INSERT INTO ELEMENT VALUES (21, 'Sc', 4, '3')");

c.execute("INSERT INTO ELEMENT VALUES (22, 'Ti', 4, '4')");
      
c.execute("INSERT INTO ELEMENT VALUES (23, 'V', 4, '5')");
      
c.execute("INSERT INTO ELEMENT VALUES (24, 'Cr', 4, '6')");

c.execute("INSERT INTO ELEMENT VALUES (25, 'Mn', 4, '7')");

c.execute("INSERT INTO ELEMENT VALUES (26, 'Fe', 4, '8')");

c.execute("INSERT INTO ELEMENT VALUES (27, 'Co', 4, '9')");
 
c.execute("INSERT INTO ELEMENT VALUES (28, 'Ni', 4, '10')");

c.execute("INSERT INTO ELEMENT VALUES (29, 'Cu', 4, '11')");

c.execute("INSERT INTO ELEMENT VALUES (30, 'Zn', 4, '12')");
      
c.execute("INSERT INTO ELEMENT VALUES (31, 'Ga', 4, '13')");
      
c.execute("INSERT INTO ELEMENT VALUES (32, 'Ge', 4, '14')");

c.execute("INSERT INTO ELEMENT VALUES (33, 'As', 4, '15')");

c.execute("INSERT INTO ELEMENT VALUES (34, 'Se', 4, '16')");

c.execute("INSERT INTO ELEMENT VALUES (35, 'Br', 4, '17')");
 
c.execute("INSERT INTO ELEMENT VALUES (36, 'Kr', 4, '18')");
 
c.execute("INSERT INTO ELEMENT VALUES (37, 'Rb', 5, '1')");

c.execute("INSERT INTO ELEMENT VALUES (38, 'Sr', 5, '2')");

c.execute("INSERT INTO ELEMENT VALUES (39, 'Y', 5, '3')");

c.execute("INSERT INTO ELEMENT VALUES (40, 'Zr', 5, '4')");
      
c.execute("INSERT INTO ELEMENT VALUES (41, 'Nb', 5, '5')");
      
c.execute("INSERT INTO ELEMENT VALUES (42, 'Mo', 5, '6')");

c.execute("INSERT INTO ELEMENT VALUES (43, 'Tc', 5, '7')");

c.execute("INSERT INTO ELEMENT VALUES (44, 'Ru', 5, '8')");

c.execute("INSERT INTO ELEMENT VALUES (45, 'Rh', 5, '9')");
 
c.execute("INSERT INTO ELEMENT VALUES (46, 'Pd', 5, '10')");

c.execute("INSERT INTO ELEMENT VALUES (47, 'Ag', 5, '11')");

c.execute("INSERT INTO ELEMENT VALUES (48, 'Cd', 5, '12')");
      
c.execute("INSERT INTO ELEMENT VALUES (49, 'In', 5, '13')");
      
c.execute("INSERT INTO ELEMENT VALUES (50, 'Sn', 5, '14')");

c.execute("INSERT INTO ELEMENT VALUES (51, 'Sb', 5, '15')");

c.execute("INSERT INTO ELEMENT VALUES (52, 'Te', 5, '16')");

c.execute("INSERT INTO ELEMENT VALUES (53, 'I', 5, '17')");
 
c.execute("INSERT INTO ELEMENT VALUES (54, 'Xe', 5, '18')");

c.execute("INSERT INTO ELEMENT VALUES (55, 'Cs', 6, '1')");

c.execute("INSERT INTO ELEMENT VALUES (56, 'Ba', 6, '2')");

c.execute("INSERT INTO ELEMENT VALUES (72, 'Hf', 6, '4')");

c.execute("INSERT INTO ELEMENT VALUES (73, 'Ta', 6, '5')");
      
c.execute("INSERT INTO ELEMENT VALUES (74, 'W', 6, '6')");
      
c.execute("INSERT INTO ELEMENT VALUES (75, 'Re', 6, '7')");

c.execute("INSERT INTO ELEMENT VALUES (76, 'Os', 6, '8')");

c.execute("INSERT INTO ELEMENT VALUES (77, 'Ir', 6, '9')");

c.execute("INSERT INTO ELEMENT VALUES (78, 'Pt', 6, '10')");
 
c.execute("INSERT INTO ELEMENT VALUES (79, 'Au', 6, '11')");

c.execute("INSERT INTO ELEMENT VALUES (80, 'Hg', 6, '12')");

c.execute("INSERT INTO ELEMENT VALUES (81, 'Tl', 6, '13')");
      
c.execute("INSERT INTO ELEMENT VALUES (82, 'Pb', 6, '14')");
      
c.execute("INSERT INTO ELEMENT VALUES (83, 'Bi', 6, '15')");

c.execute("INSERT INTO ELEMENT VALUES (84, 'Po', 6, '16')");

c.execute("INSERT INTO ELEMENT VALUES (85, 'At', 6, '17')");

c.execute("INSERT INTO ELEMENT VALUES (86, 'Rn', 6, '18')");

c.execute("INSERT INTO ELEMENT VALUES (87, 'Fr', 7, '1')");

c.execute("INSERT INTO ELEMENT VALUES (88, 'Ra', 7, '2')");

c.execute("INSERT INTO ELEMENT VALUES (104, 'Rf', 7, '4')");

c.execute("INSERT INTO ELEMENT VALUES (105, 'Db', 7, '5')");
      
c.execute("INSERT INTO ELEMENT VALUES (106, 'Sg', 7, '6')");
      
c.execute("INSERT INTO ELEMENT VALUES (107, 'Bh', 7, '7')");

c.execute("INSERT INTO ELEMENT VALUES (108, 'Hs', 7, '8')");

c.execute("INSERT INTO ELEMENT VALUES (109, 'Mt', 7, '9')");

c.execute("INSERT INTO ELEMENT VALUES (110, 'Ds', 7, '10')");
 
c.execute("INSERT INTO ELEMENT VALUES (111, 'Rg', 7, '11')");

c.execute("INSERT INTO ELEMENT VALUES (112, 'Cn', 7, '12')");

c.execute("INSERT INTO ELEMENT VALUES (113, 'Nh', 7, '13')");
      
c.execute("INSERT INTO ELEMENT VALUES (114, 'Fl', 7, '14')");
      
c.execute("INSERT INTO ELEMENT VALUES (115, 'Mc', 7, '15')");

c.execute("INSERT INTO ELEMENT VALUES (116, 'Lv', 7, '16')");

c.execute("INSERT INTO ELEMENT VALUES (117, 'Ts', 7, '17')");

c.execute("INSERT INTO ELEMENT VALUES (118, 'Og', 7, '18')");

c.execute("INSERT INTO ELEMENT VALUES (57, 'La', 9, '4')");

c.execute("INSERT INTO ELEMENT VALUES (58, 'Ce', 9, '5')");
      
c.execute("INSERT INTO ELEMENT VALUES (59, 'Pr', 9, '6')");
      
c.execute("INSERT INTO ELEMENT VALUES (60, 'Nd', 9, '7')");

c.execute("INSERT INTO ELEMENT VALUES (61, 'Pm', 9, '8')");

c.execute("INSERT INTO ELEMENT VALUES (62, 'Sm', 9, '9')");

c.execute("INSERT INTO ELEMENT VALUES (63, 'Eu', 9, '10')");
 
c.execute("INSERT INTO ELEMENT VALUES (64, 'Gd', 9, '11')");

c.execute("INSERT INTO ELEMENT VALUES (65, 'Tb', 9, '12')");

c.execute("INSERT INTO ELEMENT VALUES (66, 'Dy', 9, '13')");
      
c.execute("INSERT INTO ELEMENT VALUES (67, 'Ho', 9, '14')");
      
c.execute("INSERT INTO ELEMENT VALUES (68, 'Er', 9, '15')");

c.execute("INSERT INTO ELEMENT VALUES (69, 'Tm', 9, '16')");

c.execute("INSERT INTO ELEMENT VALUES (70, 'Yb', 9, '17')");

c.execute("INSERT INTO ELEMENT VALUES (71, 'Lu', 9, '18')");

c.execute("INSERT INTO ELEMENT VALUES (89, 'Ac', 10, '4')");

c.execute("INSERT INTO ELEMENT VALUES (90, 'Th', 10, '5')");
      
c.execute("INSERT INTO ELEMENT VALUES (91, 'Pa', 10, '6')");
      
c.execute("INSERT INTO ELEMENT VALUES (92, 'U', 10, '7')");

c.execute("INSERT INTO ELEMENT VALUES (93, 'Np', 10, '8')");

c.execute("INSERT INTO ELEMENT VALUES (94, 'Pu', 10, '9')");

c.execute("INSERT INTO ELEMENT VALUES (95, 'Am', 10, '10')");
 
c.execute("INSERT INTO ELEMENT VALUES (96, 'Cm', 10, '11')");

c.execute("INSERT INTO ELEMENT VALUES (97, 'Bk', 10, '12')");

c.execute("INSERT INTO ELEMENT VALUES (98, 'Cf', 10, '13')");
      
c.execute("INSERT INTO ELEMENT VALUES (99, 'Es', 10, '14')");
      
c.execute("INSERT INTO ELEMENT VALUES (100, 'Fm', 10, '15')");

c.execute("INSERT INTO ELEMENT VALUES (101, 'Md', 10, '16')");

c.execute("INSERT INTO ELEMENT VALUES (102, 'No', 10, '17')");

c.execute("INSERT INTO ELEMENT VALUES (103, 'Lr', 10, '18')");

c.execute("SELECT * FROM ELEMENT")

rows = c.fetchall()

for row in rows:
    print row

conn.commit()

conn.close()

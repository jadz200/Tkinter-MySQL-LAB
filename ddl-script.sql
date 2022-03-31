CREATE SCHEMA LABORATORY;
CREATE TABLE laboratory.Lab(
lno INT NOT NULL PRIMARY KEY,
lname VARCHAR(30) NOT NULL,
llocation VARCHAR(30) NOT NULL
); 
CREATE TABLE laboratory.Technician(
tno INT NOT NULL PRIMARY KEY,
tname VARCHAR(30) NOT NULL,
tjob VARCHAR(30) NOT NULL,
tmgr INT NULL,
thiredate DATE NOT NULL,
tsalary INT NOT NULL,
tbonus INT NULL,
tlno INT NOT NULL,
FOREIGN KEY (tlno) References Lab (lno),
FOREIGN KEY (tmgr) References Technician (tno)
);
INSERT laboratory.Lab VALUES(10, 'King Wood Lab', 'New York');
INSERT laboratory.Lab VALUES(20, 'Happiness Lab', 'Dallas');
INSERT laboratory.Lab VALUES(30, 'Checklist Lab', 'Chicago');
INSERT laboratory.Lab VALUES(40, 'Saint Peters Lab', 'Boston');

INSERT laboratory.Technician VALUES(7839, 'King','President', NULL, '2003-11-17 ', 6500, 0, 10);
INSERT laboratory.Technician VALUES(7566, 'Jones','Director', 7839, '2003-04-02 ', 3375, 0, 20);
INSERT laboratory.Technician VALUES(7698, 'Blake','Director', 7839, '2003-05-01 ', 3250, 0, 30);
INSERT laboratory.Technician VALUES(7782, 'Clark','Director', 7839, '2003-06-09 ', 2850, 0, 10);
INSERT laboratory.Technician VALUES(7499, 'Allen','Head Technician', 7698, '2003-02-20 ', 2000, 500, 30);
INSERT laboratory.Technician VALUES(7521, 'Ward','Head Technician', 7698, '2003-02-22 ', 1650, 800, 30);
INSERT laboratory.Technician VALUES(7654, 'Martin','Head Technician', 7698, '2003-09-28 ', 1650, 1400, 30);
INSERT laboratory.Technician VALUES(7844, 'Turner','Head Technician', 7698, '2003-09-08 ', 1900, 0, 30);
INSERT laboratory.Technician VALUES(7900, 'James','Assistant Technician', 7698, '2003-12-03 ', 1350, 0, 30);
INSERT laboratory.Technician VALUES(7788, 'Scot','Technician', 7566, '2002-06-27 ', 3500, 0, 20);
INSERT laboratory.Technician VALUES(7902, 'Ford','Technician', 7566, '2003-12-03 ', 3500, 0, 20);
INSERT laboratory.Technician VALUES(7369, 'Smith','Assistant Technician', 7902, '2002-12-17 ', 1200, 0, 20);
INSERT laboratory.Technician VALUES(7876, 'Adams','Assistant Technician', 7788, '2002-07-31 ', 1500, 0, 20);
INSERT laboratory.Technician VALUES(7934, 'Miller','Assistant Technician', 7782, '2003-01-23 ', 1700, 0, 10);

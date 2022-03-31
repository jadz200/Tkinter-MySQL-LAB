CREATE DEFINER=`root`@`localhost` PROCEDURE `exercise3`(IN labname VARCHAR(30))
BEGIN
	SELECT COUNT(tno),MIN(tsalary),AVG(tsalary),MAX(tsalary) FROM technician, LAB  WHERE lname=labname AND lno=tlno GROUP BY tlno;
END
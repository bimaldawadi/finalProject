DROP TABLE IF EXISTS `employee`;

CREATE TABLE `employee` (
  `employee_id` int(11) NOT NULL AUTO_INCREMENT,
  `employeeName` varchar(100) DEFAULT NULL,
  `employeeUsername` varchar(100) DEFAULT NULL,
  `password` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;


LOCK TABLES `employee` WRITE;

INSERT INTO `employee` (`employee_id`, `employeeName`, `employeeUsername`, `password`) VALUES (1,'Peter','1234','pwd'),(2,'jeff','456637','pwd');

UNLOCK TABLES;

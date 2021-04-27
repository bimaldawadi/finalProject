DROP TABLE IF EXISTS `customers`;

CREATE TABLE `customers` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `customerName` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `mobile` varchar(12) DEFAULT NULL,
  `customerUsername` varchar(100) DEFAULT NULL,
  `password` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;


LOCK TABLES `customer` WRITE;

INSERT INTO `customer` (`customer_id`, `customerName`, `email`, `mobile`, `customerUsername`, `password`) VALUES (1,'John','john@gmail.com','123456','123456','pwd'),(2,'bob','bob@gmail.com','98989898','1234','pwd');

UNLOCK TABLES;
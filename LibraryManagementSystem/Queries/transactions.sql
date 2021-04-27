
DROP TABLE IF EXISTS `transactions`;

CREATE TABLE `transactions` (
  `transaction_id` int(11) NOT NULL AUTO_INCREMENT,
  `customerUsername` varchar(100) DEFAULT NULL,
  `employeeUsername` varchar(100) DEFAULT NULL,
  `book_id` int(11) DEFAULT NULL,
  `issueDate` datetime DEFAULT NULL,
  `returnDate` datetime DEFAULT NULL,
  `due` int(11) DEFAULT '0',
  `Done` int(11) DEFAULT '0',
  `bookName` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`transaction_id`),
  KEY `book_id` (`book_id`),
  CONSTRAINT `transactions_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `books` (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;


LOCK TABLES `transactions` WRITE;

INSERT INTO `transactions` (`transaction_id`, `customerUsername`, `employeeUsername`, `book_id`, `issueDate`, `returnDate`, `due`, `Done`, `bookName`) VALUES (901,'1234','5678',2,'2021-04-20 18:12:05','2021-04-20 18:12:05',1,6,'A'),(100,'1234','5678',53,'2020-04-15 15:12:32','2021-04-15 15:12:32',5,2,'A');

UNLOCK TABLES;


DROP TABLE IF EXISTS `books`;

CREATE TABLE `books` (
  `book_id` int(11) NOT NULL AUTO_INCREMENT,
  `bookName` varchar(100) DEFAULT NULL,
  `author` varchar(150) DEFAULT NULL,
  `addedDate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `available` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

LOCK TABLES `books` WRITE;

INSERT INTO `books` (`book_id`, `bookName`, `author`, `addedDate`, `available`) VALUES (1,'Mike',NULL,'2015-02-18 10:12:52',5);

UNLOCK TABLES;


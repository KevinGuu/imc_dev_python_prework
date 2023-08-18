DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `username` varchar(255) DEFAULT NULL
  `user_id` 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `users` WRITE;
INSERT INTO `users` VALUES ('Bill'),('Jerry');
UNLOCK TABLES;
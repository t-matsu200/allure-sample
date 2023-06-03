use sample;

LOCK TABLES `users` WRITE;

REPLACE INTO `users` (`id`, `name`)
VALUES
	(1,'user1'),
	(2,'user2'),
	(3,'user3');

UNLOCK TABLES;

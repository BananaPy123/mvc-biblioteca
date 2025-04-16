-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: mvc
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alunos`
--

DROP TABLE IF EXISTS `alunos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alunos` (
  `id_aluno` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) DEFAULT NULL,
  `serie` varchar(10) DEFAULT NULL,
  `email` varchar(80) DEFAULT NULL,
  `senha` varchar(400) DEFAULT NULL,
  PRIMARY KEY (`id_aluno`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alunos`
--

LOCK TABLES `alunos` WRITE;
/*!40000 ALTER TABLE `alunos` DISABLE KEYS */;
INSERT INTO `alunos` VALUES (8,'Helena Ribeiro','2º Ano','helena.ribeiro@email.com','senha123'),(11,'Kaique Almeida','2º Ano','kaique.almeida@email.com','senha123'),(57,'Breno Torres','3º Ano','breno.torres@email.com','senha123'),(58,'Camila Reis','1º Ano','camila.reis@email.com','senha123'),(59,'Diego Cardoso','2º Ano','diego.cardoso@email.com','senha123');
/*!40000 ALTER TABLE `alunos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emprestimos`
--

DROP TABLE IF EXISTS `emprestimos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emprestimos` (
  `id_emprestimos` int NOT NULL AUTO_INCREMENT,
  `id_aluno` int DEFAULT NULL,
  `id_livro` int DEFAULT NULL,
  `data_emprestimo` varchar(10) DEFAULT NULL,
  `data_devolucao` varchar(10) DEFAULT NULL,
  `devolvido` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id_emprestimos`),
  KEY `fk_aluno` (`id_aluno`),
  CONSTRAINT `fk_aluno` FOREIGN KEY (`id_aluno`) REFERENCES `alunos` (`id_aluno`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emprestimos`
--

LOCK TABLES `emprestimos` WRITE;
/*!40000 ALTER TABLE `emprestimos` DISABLE KEYS */;
INSERT INTO `emprestimos` VALUES (1,8,1,'2025-04-16',NULL,0),(2,11,9,'2025-04-16',NULL,0),(3,11,9,'16-04-2025','20-04-2025',1),(4,57,11,'2025-04-16','2025-04-26',1),(5,58,3,'2025-04-16','2025-04-17',1),(6,59,15,'2025-04-16','2025-04-30',1);
/*!40000 ALTER TABLE `emprestimos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `livros`
--

DROP TABLE IF EXISTS `livros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `livros` (
  `id_livro` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(40) DEFAULT NULL,
  `autor` tinytext,
  `data_publicacao` varchar(10) DEFAULT NULL,
  `isbn` varchar(20) DEFAULT NULL,
  `pfd_link` text,
  `descricao` text,
  `capa` varchar(700) DEFAULT NULL,
  PRIMARY KEY (`id_livro`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `livros`
--

LOCK TABLES `livros` WRITE;
/*!40000 ALTER TABLE `livros` DISABLE KEYS */;
INSERT INTO `livros` VALUES (1,'Cylindrical Antennas and Arrays','Ronold W. P. King, George J. Fikioris, Richard B. Mack','2002-10-10','9781139437097',NULL,'This book explains how to design, analyse and test cylindrical antenna arrays from a practical engineering standpoint. Written by three of the leading engineers in the field, this book is destined to become established as the basic reference in the field for many years to come.',NULL),(9,'Arrays','Eu',NULL,'5435235423',NULL,'araerlhbsdakjvbdajslkbvas',NULL),(18,'As infinitas vidas de Dylan Reynolds','Sarah Pires Barreirinhas','2020-07-21','9786556250212',NULL,'Eu sabia sobre sua dor. De como penetrava sua pele, tornando-se parte de seu corpo, misturando-se com o sangue de suas veias. Eu sabia o quanto queria viver e o quanto estava esforçando-se para isso. Eu sabia muito sobre ele. Mas o que eu não sabia era como seria sua história se não tivesse morrido naquela tarde. Não é sobre o que foi, mas o que poderia ter sido. Livro de estreia de Sarah Pires Barreirinhas, As infinitas vidas de Dylan Reynolds é exemplo de uma nova geração de romances: não apenas ressalta a complexidade do universo interior adolescente, repleto de inseguranças, lutas, dores e amores, mas denuncia uma sociedade injusta, que parece mais preocupada em cobrar padrões do que aceitar diferenças. Com personagens envolventes e realistas, a obra traz um enredo intrigante que prenderá o leitor até a última página.','http://books.google.com/books/content?id=yGXyDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api'),(19,'Razão e sensibilidade','Jane Austen','2015-11-06','9788577994953',NULL,'Este romance concentra sua narrativa nas idílicas tramas de amor e desilusão em que duas belas irmãs inglesas se envolvem - Elinor e Marianne Dashwood - quando chega a idade do casamento. À procura do amor verdadeiro, as filhas órfãs de uma família pertencente à pequena nobreza enfrentam o mundo repleto de interesses e intrigas da alta aristocracia. Marianne e Elinor representam polos opostos do universo ético de Austen - enquanto Marianne é romântica, musical e dada a rompantes de espontaneidade, Elinor é a encarnação da prudência e do decoro.','http://books.google.com/books/content?id=KgblCgAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api'),(20,'PHP','Tim Converse, JOYCE PARK','2003','9788535211306',NULL,NULL,'http://books.google.com/books/content?id=_xv1frKVlp8C&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api');
/*!40000 ALTER TABLE `livros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `professores`
--

DROP TABLE IF EXISTS `professores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `professores` (
  `id_professor` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(60) DEFAULT NULL,
  `cpf` varchar(20) DEFAULT NULL,
  `email` varchar(80) DEFAULT NULL,
  `senha` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id_professor`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `professores`
--

LOCK TABLES `professores` WRITE;
/*!40000 ALTER TABLE `professores` DISABLE KEYS */;
INSERT INTO `professores` VALUES (1,'Fernando','12345678901','fernando@gmail.com','senha123'),(2,'Fernando','12345678901','fernando@gmail.com','senha123'),(3,'ALEF DE SOUZA SOBRINHO','96686943096','aluno2@gmail.com','alef1234'),(5,'Marcos','12345678901','marquesTeste1@gmail.com','33a55ce3bd6606437c71a69a15cee2c6'),(6,'Nicole','55739870038','nicole@gmail.com','82044515b2229452ed41bcbbbac6c3c8'),(7,'cleo','55739870038','cleo@gmail.com','0e66d886a4a314480278ed894898eb1b'),(8,'marques','12321321321','marques@gmail.com','25962fc8f19560c086f412e89a72f05c'),(9,'Marcos Miguel de Souza Sobrinho','050.713.470-24','marcosmiguel@gmail.com','33a55ce3bd6606437c71a69a15cee2c6'),(10,'Alef de Souza Sobrinho','1928783829','alefsouza@gmail.com ','c024d8645565ab377d3fa52d54f543c4'),(11,'renato','213412432143','renato@gmail.com','pbkdf2:sha256:1000000$vhTf6MNAMIBuQ8kG$0779b07fb90cdcc40395dfd750f735bfa9190f397a41321fa4d6c85b93c4814b');
/*!40000 ALTER TABLE `professores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tentativas_login`
--

DROP TABLE IF EXISTS `tentativas_login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tentativas_login` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `ip` varchar(45) NOT NULL,
  `sucesso` tinyint(1) NOT NULL,
  `data_hora` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tentativas_login`
--

LOCK TABLES `tentativas_login` WRITE;
/*!40000 ALTER TABLE `tentativas_login` DISABLE KEYS */;
INSERT INTO `tentativas_login` VALUES (1,'marcosmiguel@gmail.com','127.0.0.1',0,'2025-04-16 18:12:58'),(2,'marcosmiguel@gmail.com','127.0.0.1',0,'2025-04-16 18:13:03'),(3,'marcosmiguel@gmail.com','127.0.0.1',0,'2025-04-16 18:13:13'),(4,'marcosmiguel@gmail.com','127.0.0.1',0,'2025-04-16 18:15:30'),(5,'marcosmiguel@gmail.com','127.0.0.1',0,'2025-04-16 19:26:39'),(6,'marcosmiguel@gmail.com','127.0.0.1',0,'2025-04-16 21:22:11');
/*!40000 ALTER TABLE `tentativas_login` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-16 19:03:37

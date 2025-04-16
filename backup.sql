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
  `senha` varchar(36) DEFAULT NULL,
  PRIMARY KEY (`id_aluno`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alunos`
--

LOCK TABLES `alunos` WRITE;
/*!40000 ALTER TABLE `alunos` DISABLE KEYS */;
INSERT INTO `alunos` VALUES (4,'Daniela silva Souza','1º Ano','daniela.silva.souza@email.com','senha123'),(5,'Eduardo Mendes','2º Ano','eduardo.mendes@email.com','senha123'),(6,'Fernanda Rocha','3º Ano','fernanda.rocha@email.com','senha123'),(7,'Gabriel Freitas','1º Ano','gabriel.freitas@email.com','senha123'),(8,'Helena Ribeiro','2º Ano','helena.ribeiro@email.com','senha123'),(9,'Igor Martins','3º Ano','igor.martins@email.com','senha123'),(10,'Juliana Dias','1º Ano','juliana.dias@email.com','senha123'),(11,'Kaique Almeida','2º Ano','kaique.almeida@email.com','senha123'),(12,'Larissa Lopes','3º Ano','larissa.lopes@email.com','senha123'),(13,'Marcos Oliveira','1º Ano','marcos.oliveira@email.com','senha123'),(14,'Nathalia Fernandes','2º Ano','nathalia.fernandes@email.com','senha123'),(15,'Otávio Teixeira','3º Ano','otavio.teixeira@email.com','senha123'),(16,'Paula Nunes','1º Ano','paula.nunes@email.com','senha123'),(17,'Rafael Santos','2º Ano','rafael.santos@email.com','senha123'),(18,'Sabrina Castro','3º Ano','sabrina.castro@email.com','senha123'),(19,'Thiago Moreira','1º Ano','thiago.moreira@email.com','senha123'),(20,'Ursula Andrade','2º Ano','ursula.andrade@email.com','senha123'),(21,'Vinicius Pinto','3º Ano','vinicius.pinto@email.com','senha123'),(22,'Wesley Duarte','1º Ano','wesley.duarte@email.com','senha123'),(23,'Xuxa Barbosa','2º Ano','xuxa.barbosa@email.com','senha123'),(24,'Yasmin Gomes','3º Ano','yasmin.gomes@email.com','senha123'),(25,'Zeca Ferreira','1º Ano','zeca.ferreira@email.com','senha123'),(26,'Alana Brito','2º Ano','alana.brito@email.com','senha123'),(27,'Breno Torres','3º Ano','breno.torres@email.com','senha123'),(28,'Camila Reis','1º Ano','camila.reis@email.com','senha123'),(29,'Diego Cardoso','2º Ano','diego.cardoso@email.com','senha123'),(30,'Elaine Pires','3º Ano','elaine.pires@email.com','senha123'),(34,'Daniela silva Souza','1º Ano','daniela.silva.souza@email.com','senha123'),(35,'Eduardo Mendes','2º Ano','eduardo.mendes@email.com','senha123'),(36,'Fernanda Rocha','3º Ano','fernanda.rocha@email.com','senha123'),(37,'Gabriel Freitas','1º Ano','gabriel.freitas@email.com','senha123'),(38,'Helena Ribeiro','2º Ano','helena.ribeiro@email.com','senha123'),(39,'Igor Martins','3º Ano','igor.martins@email.com','senha123'),(40,'Juliana Dias','1º Ano','juliana.dias@email.com','senha123'),(41,'Kaique Almeida','2º Ano','kaique.almeida@email.com','senha123'),(42,'Larissa Lopes','3º Ano','larissa.lopes@email.com','senha123'),(43,'Marcos Oliveira','1º Ano','marcos.oliveira@email.com','senha123'),(44,'Nathalia Fernandes','2º Ano','nathalia.fernandes@email.com','senha123'),(45,'Otávio Teixeira','3º Ano','otavio.teixeira@email.com','senha123'),(46,'Paula Nunes','1º Ano','paula.nunes@email.com','senha123'),(47,'Rafael Santos','2º Ano','rafael.santos@email.com','senha123'),(48,'Sabrina Castro','3º Ano','sabrina.castro@email.com','senha123'),(49,'Thiago Moreira','1º Ano','thiago.moreira@email.com','senha123'),(50,'Ursula Andrade','2º Ano','ursula.andrade@email.com','senha123'),(51,'Vinicius Pinto','3º Ano','vinicius.pinto@email.com','senha123'),(52,'Wesley Duarte','1º Ano','wesley.duarte@email.com','senha123'),(53,'Xuxa Barbosa','2º Ano','xuxa.barbosa@email.com','senha123'),(54,'Yasmin Gomes','3º Ano','yasmin.gomes@email.com','senha123'),(55,'Zeca Ferreira','1º Ano','zeca.ferreira@email.com','senha123'),(56,'Alana Brito','2º Ano','alana.brito@email.com','senha123'),(57,'Breno Torres','3º Ano','breno.torres@email.com','senha123'),(58,'Camila Reis','1º Ano','camila.reis@email.com','senha123'),(59,'Diego Cardoso','2º Ano','diego.cardoso@email.com','senha123'),(60,'Elaine Pires','3º Ano','elaine.pires@email.com','senha123'),(61,'Alef','3D','alefs@gmail.com','c024d8645565ab377d3fa52d54f543c4'),(62,'nicole','','','d41d8cd98f00b204e9800998ecf8427e'),(63,'nicole','','','d41d8cd98f00b204e9800998ecf8427e'),(64,'nicole','3A','nicole@gmail.com','82044515b2229452ed41bcbbbac6c3c8'),(65,'nicole','3A','nicole@gmail.com','82044515b2229452ed41bcbbbac6c3c8');
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
  `data_emrpestimo` date DEFAULT NULL,
  `data_devolucao` date DEFAULT NULL,
  `devolvido` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id_emprestimos`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emprestimos`
--

LOCK TABLES `emprestimos` WRITE;
/*!40000 ALTER TABLE `emprestimos` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `livros`
--

LOCK TABLES `livros` WRITE;
/*!40000 ALTER TABLE `livros` DISABLE KEYS */;
INSERT INTO `livros` VALUES (1,'Cylindrical Antennas and Arrays','Ronold W. P. King, George J. Fikioris, Richard B. Mack','2002-10-10','9781139437097',NULL,'This book explains how to design, analyse and test cylindrical antenna arrays from a practical engineering standpoint. Written by three of the leading engineers in the field, this book is destined to become established as the basic reference in the field for many years to come.',NULL),(2,'operadores aritméticos','Eu',NULL,NULL,NULL,NULL,NULL),(3,'Dom casmurro',NULL,NULL,NULL,NULL,NULL,NULL),(4,'orgulho e preconceito',NULL,NULL,NULL,NULL,NULL,NULL),(5,'As infinitas vidas de Dylan Reynolds','Sarah Pires Barreirinhas','2020-07-21','9786556250212',NULL,'Eu sabia sobre sua dor. De como penetrava sua pele, tornando-se parte de seu corpo, misturando-se com o sangue de suas veias. Eu sabia o quanto queria viver e o quanto estava esforçando-se para isso. Eu sabia muito sobre ele. Mas o que eu não sabia era como seria sua história se não tivesse morrido naquela tarde. Não é sobre o que foi, mas o que poderia ter sido. Livro de estreia de Sarah Pires Barreirinhas, As infinitas vidas de Dylan Reynolds é exemplo de uma nova geração de romances: não apenas ressalta a complexidade do universo interior adolescente, repleto de inseguranças, lutas, dores e amores, mas denuncia uma sociedade injusta, que parece mais preocupada em cobrar padrões do que aceitar diferenças. Com personagens envolventes e realistas, a obra traz um enredo intrigante que prenderá o leitor até a última página.',NULL),(6,'As infinitas vidas de Dylan Reynolds','Sarah Pires Barreirinhas','2020-07-21','9786556250212',NULL,'Eu sabia sobre sua dor. De como penetrava sua pele, tornando-se parte de seu corpo, misturando-se com o sangue de suas veias. Eu sabia o quanto queria viver e o quanto estava esforçando-se para isso. Eu sabia muito sobre ele. Mas o que eu não sabia era como seria sua história se não tivesse morrido naquela tarde. Não é sobre o que foi, mas o que poderia ter sido. Livro de estreia de Sarah Pires Barreirinhas, As infinitas vidas de Dylan Reynolds é exemplo de uma nova geração de romances: não apenas ressalta a complexidade do universo interior adolescente, repleto de inseguranças, lutas, dores e amores, mas denuncia uma sociedade injusta, que parece mais preocupada em cobrar padrões do que aceitar diferenças. Com personagens envolventes e realistas, a obra traz um enredo intrigante que prenderá o leitor até a última página.',NULL),(7,'dom casmu',NULL,NULL,NULL,NULL,NULL,NULL),(8,'operadores',NULL,NULL,NULL,NULL,NULL,NULL),(9,'Arrays',NULL,NULL,NULL,NULL,NULL,NULL),(10,'Cylindrical Antennas and Arrays','Ronold W. P. King, George J. Fikioris, Richard B. Mack','2002-10-10','9781139437097',NULL,'This book explains how to design, analyse and test cylindrical antenna arrays from a practical engineering standpoint. Written by three of the leading engineers in the field, this book is destined to become established as the basic reference in the field for many years to come.',NULL),(11,'Cylindrical Antennas and Arrays','Ronold W. P. King, George J. Fikioris, Richard B. Mack','2002-10-10','9781139437097',NULL,'This book explains how to design, analyse and test cylindrical antenna arrays from a practical engineering standpoint. Written by three of the leading engineers in the field, this book is destined to become established as the basic reference in the field for many years to come.',NULL),(12,'Cylindrical Antennas and Arrays','Ronold W. P. King, George J. Fikioris, Richard B. Mack','2002-10-10','9781139437097',NULL,'This book explains how to design, analyse and test cylindrical antenna arrays from a practical engineering standpoint. Written by three of the leading engineers in the field, this book is destined to become established as the basic reference in the field for many years to come.',NULL),(13,'Cylindrical Antennas and Arrays','Ronold W. P. King, George J. Fikioris, Richard B. Mack','2002-10-10','9781139437097',NULL,'This book explains how to design, analyse and test cylindrical antenna arrays from a practical engineering standpoint. Written by three of the leading engineers in the field, this book is destined to become established as the basic reference in the field for many years to come.',NULL),(14,'Orgulho e Preconceito',NULL,NULL,NULL,NULL,NULL,NULL),(15,'As infinitas vidas de Dylan Reynolds','Sarah Pires Barreirinhas','2020-07-21','9786556250212',NULL,'Eu sabia sobre sua dor. De como penetrava sua pele, tornando-se parte de seu corpo, misturando-se com o sangue de suas veias. Eu sabia o quanto queria viver e o quanto estava esforçando-se para isso. Eu sabia muito sobre ele. Mas o que eu não sabia era como seria sua história se não tivesse morrido naquela tarde. Não é sobre o que foi, mas o que poderia ter sido. Livro de estreia de Sarah Pires Barreirinhas, As infinitas vidas de Dylan Reynolds é exemplo de uma nova geração de romances: não apenas ressalta a complexidade do universo interior adolescente, repleto de inseguranças, lutas, dores e amores, mas denuncia uma sociedade injusta, que parece mais preocupada em cobrar padrões do que aceitar diferenças. Com personagens envolventes e realistas, a obra traz um enredo intrigante que prenderá o leitor até a última página.',NULL),(16,'As infinitas vidas de Dylan Reynolds','Sarah Pires Barreirinhas','2020-07-21','9786556250212',NULL,'Eu sabia sobre sua dor. De como penetrava sua pele, tornando-se parte de seu corpo, misturando-se com o sangue de suas veias. Eu sabia o quanto queria viver e o quanto estava esforçando-se para isso. Eu sabia muito sobre ele. Mas o que eu não sabia era como seria sua história se não tivesse morrido naquela tarde. Não é sobre o que foi, mas o que poderia ter sido. Livro de estreia de Sarah Pires Barreirinhas, As infinitas vidas de Dylan Reynolds é exemplo de uma nova geração de romances: não apenas ressalta a complexidade do universo interior adolescente, repleto de inseguranças, lutas, dores e amores, mas denuncia uma sociedade injusta, que parece mais preocupada em cobrar padrões do que aceitar diferenças. Com personagens envolventes e realistas, a obra traz um enredo intrigante que prenderá o leitor até a última página.',NULL);
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
  `senha` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id_professor`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `professores`
--

LOCK TABLES `professores` WRITE;
/*!40000 ALTER TABLE `professores` DISABLE KEYS */;
INSERT INTO `professores` VALUES (1,'Fernando','12345678901','fernando@gmail.com','senha123'),(2,'Fernando','12345678901','fernando@gmail.com','senha123'),(3,'ALEF DE SOUZA SOBRINHO','96686943096','aluno2@gmail.com','alef1234'),(5,'Marcos','12345678901','marquesTeste1@gmail.com','33a55ce3bd6606437c71a69a15cee2c6'),(6,'Nicole','55739870038','nicole@gmail.com','82044515b2229452ed41bcbbbac6c3c8'),(7,'cleo','55739870038','cleo@gmail.com','0e66d886a4a314480278ed894898eb1b'),(8,'marques','12321321321','marques@gmail.com','25962fc8f19560c086f412e89a72f05c'),(9,'Marcos Miguel de Souza Sobrinho','050.713.470-24','marcosmiguel@gmail.com','33a55ce3bd6606437c71a69a15cee2c6'),(10,'Alef de Souza Sobrinho','1928783829','alefsouza@gmail.com ','c024d8645565ab377d3fa52d54f543c4');
/*!40000 ALTER TABLE `professores` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-15 21:15:49

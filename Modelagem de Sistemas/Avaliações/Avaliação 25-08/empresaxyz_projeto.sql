CREATE DATABASE  IF NOT EXISTS `empresaxyz` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `empresaxyz`;
-- MySQL dump 10.13  Distrib 5.6.11, for Win32 (x86)
--
-- Host: 127.0.0.1    Database: empresaxyz
-- ------------------------------------------------------
-- Server version	5.5.20-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `projeto`
--

DROP TABLE IF EXISTS `projeto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `projeto` (
  `codigo` int(5) NOT NULL,
  `datainicio` date NOT NULL,
  `datafim` date NOT NULL,
  `descricao` varchar(50) NOT NULL,
  `valor` float NOT NULL,
  `codfunc` int(5) NOT NULL,
  `codsetor` int(5) NOT NULL,
  PRIMARY KEY (`codigo`),
  KEY `codfunc` (`codfunc`),
  KEY `codsetor` (`codsetor`),
  CONSTRAINT `projeto_ibfk_1` FOREIGN KEY (`codfunc`) REFERENCES `funcionario` (`codigo`),
  CONSTRAINT `projeto_ibfk_2` FOREIGN KEY (`codsetor`) REFERENCES `setor` (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projeto`
--

LOCK TABLES `projeto` WRITE;
/*!40000 ALTER TABLE `projeto` DISABLE KEYS */;
INSERT INTO `projeto` VALUES (4,'2023-08-10','2023-09-10','Asfaltar a rua Churusbamgo Churusbago',345000,6,4),(8,'2022-08-22','2023-06-23','Finilizar as peças no prazo',10000,5,1),(9,'2023-06-28','2023-09-28','Finilizar os revisão  das peças no prazo',20000,6,2),(10,'2023-10-25','2024-02-25','Finilizar a vistoria no prazo',30000,7,3);
/*!40000 ALTER TABLE `projeto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-25 15:07:58

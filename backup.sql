-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.20.04.1

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
-- Table structure for table `Admin_Register`
--

DROP TABLE IF EXISTS `Admin_Register`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Admin_Register` (
  `ID_No` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(225) NOT NULL,
  `Surname` varchar(225) DEFAULT NULL,
  `Phone_No` varchar(225) NOT NULL,
  `Password` varchar(225) NOT NULL,
  `Next_of_kin_Fullname` varchar(225) NOT NULL,
  `Next_of_kin_Phone_No` varchar(225) NOT NULL,
  `ID_number` varchar(225) NOT NULL,
  `Register_DateTime` varchar(225) NOT NULL,
  PRIMARY KEY (`ID_No`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin_Register`
--

LOCK TABLES `Admin_Register` WRITE;
/*!40000 ALTER TABLE `Admin_Register` DISABLE KEYS */;
INSERT INTO `Admin_Register` VALUES (1,'Philile','Majola','0657868809','8-2fermENt2020P1','Olisa Berend','0783345432','8906275328789','2021-07-28 12:26:1627468012');
/*!40000 ALTER TABLE `Admin_Register` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Logins`
--

DROP TABLE IF EXISTS `Logins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Logins` (
  `ID_No` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(225) NOT NULL,
  `Password` varchar(225) NOT NULL,
  `Login_DateTime` varchar(225) NOT NULL,
  PRIMARY KEY (`ID_No`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Logins`
--

LOCK TABLES `Logins` WRITE;
/*!40000 ALTER TABLE `Logins` DISABLE KEYS */;
INSERT INTO `Logins` VALUES (1,'Zipho','Crf6ZS@#LCA','2021-07-28 14:16:1627474592');
/*!40000 ALTER TABLE `Logins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Logouts`
--

DROP TABLE IF EXISTS `Logouts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Logouts` (
  `ID_No` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(225) NOT NULL,
  `Password` varchar(225) NOT NULL,
  `Logout_DateTime` varchar(225) NOT NULL,
  PRIMARY KEY (`ID_No`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Logouts`
--

LOCK TABLES `Logouts` WRITE;
/*!40000 ALTER TABLE `Logouts` DISABLE KEYS */;
INSERT INTO `Logouts` VALUES (1,'Zipho','Crf6ZS@#LCA','2021-07-28 14:16:1627474592');
/*!40000 ALTER TABLE `Logouts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Register`
--

DROP TABLE IF EXISTS `Register`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Register` (
  `ID_No` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(225) NOT NULL,
  `Surname` varchar(225) DEFAULT NULL,
  `Phone_No` varchar(225) NOT NULL,
  `Password` varchar(225) NOT NULL,
  `Next_of_kin_Fullname` varchar(225) NOT NULL,
  `Next_of_kin_Phone_No` varchar(225) NOT NULL,
  `ID_number` varchar(225) NOT NULL,
  `Register_DateTime` varchar(225) NOT NULL,
  PRIMARY KEY (`ID_No`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Register`
--

LOCK TABLES `Register` WRITE;
/*!40000 ALTER TABLE `Register` DISABLE KEYS */;
INSERT INTO `Register` VALUES (1,'Zipho','Sithandathu','0633498809','Crf6ZS@#LCA','Tsepelang Kosa','0780013352','9905175329087','2021-07-28 11:24:1627464262');
/*!40000 ALTER TABLE `Register` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mytable`
--

DROP TABLE IF EXISTS `mytable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mytable` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mytable`
--

LOCK TABLES `mytable` WRITE;
/*!40000 ALTER TABLE `mytable` DISABLE KEYS */;
INSERT INTO `mytable` VALUES (1,'myuser','sithandathuzipho@gmail.com');
/*!40000 ALTER TABLE `mytable` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-29 13:29:18

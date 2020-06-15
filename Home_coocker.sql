-- MySQL dump 10.13  Distrib 5.7.8-rc, for Linux (x86_64)
--
-- Host: localhost    Database: HomeCooker_db
-- ------------------------------------------------------
-- Server version	5.7.8-rc

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
-- Table structure for table `Recipes`
--

DROP TABLE IF EXISTS `Recipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Recipes` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `name` varchar(128) NOT NULL,
  `text` varchar(2048) NOT NULL,
  `user_id` varchar(60) DEFAULT NULL,
  `review` int(11) DEFAULT NULL,
  `ingredients` varchar(1024) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `Recipes_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Recipes`
--

LOCK TABLES `Recipes` WRITE;
/*!40000 ALTER TABLE `Recipes` DISABLE KEYS */;
INSERT INTO `Recipes` VALUES ('03d71d9f-fbb5-4d8a-afb7-02ac8d4f47c9','2020-06-15 21:01:39','2020-06-15 21:01:39','Pastas al Nido','Empieza cocinando la pasta en abundante agua con sal junto al huevo y el pollo, en una olla calienta un poco de aceite e inserta la cebolla picada hasta que dore, posteriormente, agrega el tomate y el pollo desmechado para formar el guiso salpimentando a tu gusto. Cuando la pasta esté lista, agregala a la olla del guiso, revuelvela bien y está lista para servir. Para la presentación de nido debes agregar el queso parmesano de forma circular cerca del centro del plato, si lo deseas puedes agregar oregano para darle tonos verdes; para terminar ubica el huevo en el centro del plato.','9a47049c-cf6a-4478-abee-b23a333fbee4',1,'200g de pasta, un huevo, una pechuga de pollo, una cebolla pequeña, un tomate pequeño, queso parmesano, sal y pimienta al gusto.'),('3142e441-c995-4d98-8f10-cbc3caddad11','2020-06-15 22:17:13','2020-06-15 22:17:13','Copa caprichosa','Triture las galletas hasta hacerlas polvo y mezclelas bien con la mantequilla derretida, en una copa agrege una capa de la mezcla de galletas a su al rededor para formar la corteza, separe una parte del postre de tres leches y mezclelo con la mitad de la gelatina sin sabor, viertalo en la copa hasta la mitad e incorpore a la nevera. Pasadas una o dos horas, mezcle el resto del postre de tres leches con el zumo de fruta e integre con el resto de la gelatina (si se desea se puede colocar una capa de galletas molidas), vierta esta mezcla sobre la copa teniendo cuidado de no mezclar mucho los dos postres y vuelva a meter a la nevera. Se puede decorar con fruta cortada y galletas.','99a6d4af-5a15-4975-9b58-9973441388ba',3,'Un cuarto de taza de zumo de fruta preferido preferiblemente ácido. Tres cuartos de taza de postre de tres leches. Una cucharada de gelatina sin sabor. Dos cucharadas de mantequilla. Galletas dulces.'),('7f3c812b-f49a-4e28-9fa7-0e323e6cc80a','2020-06-15 21:42:07','2020-06-15 21:42:07','Brownie con helado','Colocar el brownie en el horno microondas por 10 segundos, posteriormente colocarle una bola de helado de su sabor favorito','9a47049c-cf6a-4478-abee-b23a333fbee4',3,'1 Brownie. 1 Bola de helado'),('8b6d0077-0f83-423a-9d10-98cdcdfc21f1','2020-06-15 21:33:40','2020-06-15 21:33:40','Cebiche de camaron','Mezcle los camarones, la cebolla y el limon; cubra y deje marinar una horas. Escurra parte del jugo, agrege cilantro, la salsa de tomate, el aji y la sal. Revuelva y sirva. Acompañar con galletas','99a6d4af-5a15-4975-9b58-9973441388ba',5,'2 Libras de camarón tigre. 1 Taza de jugo de limon. 1 Taza de cebolla cabezona finamente picada. Media taza de cilantro. 2 Tazas de salsa de tomate. Aji y sal al gusto.'),('8b71097d-bd0b-4ee9-9d55-c212d82703de','2020-06-15 21:58:18','2020-06-15 21:58:18','Postre de tres leches','Mezclar las tres leches en la licuadora, licuar con la gelatina sin sabor verter en moldes y dejar enfriar al menos 4 horas.','9a47049c-cf6a-4478-abee-b23a333fbee4',3,'1 Bolsa de leche. 1 Lata de crema de leche. 1 Lata de leche condensada. 2 Cucharadas de gelatina sin sabor.');
/*!40000 ALTER TABLE `Recipes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Reviews`
--

DROP TABLE IF EXISTS `Reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Reviews` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `text` varchar(1024) NOT NULL,
  `rating` int(11) NOT NULL,
  `user_id` varchar(60) DEFAULT NULL,
  `recipe_id` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `recipe_id` (`recipe_id`),
  CONSTRAINT `Reviews_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`),
  CONSTRAINT `Reviews_ibfk_2` FOREIGN KEY (`recipe_id`) REFERENCES `Recipes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Reviews`
--

LOCK TABLES `Reviews` WRITE;
/*!40000 ALTER TABLE `Reviews` DISABLE KEYS */;
INSERT INTO `Reviews` VALUES ('4ad27e1a-83b8-41fe-a8e1-f79b63ceb828','2020-06-15 22:02:17','2020-06-15 22:02:17','Un poco sencillo pero clásico',3,'c040233a-f7c5-4e2e-9561-8ffb48ff78ee','7f3c812b-f49a-4e28-9fa7-0e323e6cc80a'),('75429d4f-e820-4b83-9a88-d8ef6f40319b','2020-06-15 22:02:58','2020-06-15 22:02:58','Buena y extraña',4,'c040233a-f7c5-4e2e-9561-8ffb48ff78ee','03d71d9f-fbb5-4d8a-afb7-02ac8d4f47c9'),('fb10af10-1003-4d94-bcd6-ecc4fd9fe6d0','2020-06-15 22:03:51','2020-06-15 22:03:51','Sencilla y Clásica',3,'df08d0ef-cdbc-4ca1-b9de-992ef2fad71d','7f3c812b-f49a-4e28-9fa7-0e323e6cc80a');
/*!40000 ALTER TABLE `Reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Users` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `first_name` varchar(128) DEFAULT NULL,
  `last_name` varchar(128) DEFAULT NULL,
  `website` varchar(256) DEFAULT NULL,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `user_type` int(11) NOT NULL,
  `profile_image` blob,
  `nickname` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES ('115ac6b2-6d1d-448d-8752-bbfa8ce87bc7','2020-06-15 22:19:56','2020-06-15 22:19:56','Home dev name','Home dev last name','Home website','home dev@HomeCooker.com','5b18783cce61377f55f068dc42210e0f',1,NULL,'Home nick'),('99a6d4af-5a15-4975-9b58-9973441388ba','2020-06-15 21:06:21','2020-06-15 21:06:21',NULL,NULL,NULL,'zulsb@gmail.com','827ccb0eea8a706c4c34a16891f84e7b',1,NULL,'Luz'),('9a47049c-cf6a-4478-abee-b23a333fbee4','2020-06-15 20:47:26','2020-06-15 20:47:26',NULL,NULL,'marcoant.tech','acalde27@hotmail.com','93593ee79065534f06fa636d79509c40',1,NULL,'MarcoAnt'),('c040233a-f7c5-4e2e-9561-8ffb48ff78ee','2020-06-15 21:07:16','2020-06-15 21:07:16','Jesús',NULL,NULL,'yisus@yourhearth.com','1e01ba3e07ac48cbdab2d3284d1dd0fa',0,NULL,'Yisus'),('df08d0ef-cdbc-4ca1-b9de-992ef2fad71d','2020-06-15 21:05:03','2020-06-15 21:05:03',NULL,NULL,NULL,'jsebastian.garcia1995@gmail.com','b95505294ff86414970f00b4afe639e9',0,NULL,'Noah');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-15 22:22:12

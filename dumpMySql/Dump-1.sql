--
-- Current Database: `pobedin88_tbot`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `pobedin88_tbot` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `pobedin88_tbot`;

-- MySQL dump 10.13  Distrib 5.7.12, for Win32 (AMD64)
--
-- Host: pobedin88.beget.tech    Database: pobedin88_tbot
-- ------------------------------------------------------
-- Server version	5.7.21-20-beget-5.7.21-20-1-log

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
-- Table structure for table `auth_group`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'Бот');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(7,1,7),(8,1,8),(9,1,9),(10,1,10),(11,1,11),(12,1,12),(13,1,13),(14,1,14),(15,1,15),(16,1,16),(17,1,17),(18,1,18),(19,1,19),(20,1,20),(21,1,21),(22,1,22),(23,1,23),(24,1,24),(25,1,25),(26,1,26),(27,1,27),(28,1,28),(29,1,29),(30,1,30),(31,1,31),(32,1,32),(33,1,33),(34,1,34),(35,1,35),(36,1,36),(37,1,37),(38,1,38),(39,1,39),(40,1,40),(41,1,41),(42,1,42),(43,1,43),(44,1,44),(45,1,45),(46,1,46),(47,1,47),(48,1,48),(49,1,49),(50,1,50),(51,1,51),(52,1,52),(53,1,53),(54,1,54),(55,1,55),(56,1,56),(57,1,57),(58,1,58),(59,1,59),(60,1,60),(61,1,61),(62,1,62),(63,1,63);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add auth group',7,'add_authgroup'),(20,'Can change auth group',7,'change_authgroup'),(21,'Can delete auth group',7,'delete_authgroup'),(22,'Can add auth group permissions',8,'add_authgrouppermissions'),(23,'Can change auth group permissions',8,'change_authgrouppermissions'),(24,'Can delete auth group permissions',8,'delete_authgrouppermissions'),(25,'Can add auth permission',9,'add_authpermission'),(26,'Can change auth permission',9,'change_authpermission'),(27,'Can delete auth permission',9,'delete_authpermission'),(28,'Can add auth user',10,'add_authuser'),(29,'Can change auth user',10,'change_authuser'),(30,'Can delete auth user',10,'delete_authuser'),(31,'Can add auth user groups',11,'add_authusergroups'),(32,'Can change auth user groups',11,'change_authusergroups'),(33,'Can delete auth user groups',11,'delete_authusergroups'),(34,'Can add auth user user permissions',12,'add_authuseruserpermissions'),(35,'Can change auth user user permissions',12,'change_authuseruserpermissions'),(36,'Can delete auth user user permissions',12,'delete_authuseruserpermissions'),(37,'Can add django admin log',13,'add_djangoadminlog'),(38,'Can change django admin log',13,'change_djangoadminlog'),(39,'Can delete django admin log',13,'delete_djangoadminlog'),(40,'Can add django content type',14,'add_djangocontenttype'),(41,'Can change django content type',14,'change_djangocontenttype'),(42,'Can delete django content type',14,'delete_djangocontenttype'),(43,'Can add django migrations',15,'add_djangomigrations'),(44,'Can change django migrations',15,'change_djangomigrations'),(45,'Can delete django migrations',15,'delete_djangomigrations'),(46,'Can add django session',16,'add_djangosession'),(47,'Can change django session',16,'change_djangosession'),(48,'Can delete django session',16,'delete_djangosession'),(49,'Can add events descript',17,'add_eventsdescript'),(50,'Can change events descript',17,'change_eventsdescript'),(51,'Can delete events descript',17,'delete_eventsdescript'),(52,'Can add events gift',18,'add_eventsgift'),(53,'Can change events gift',18,'change_eventsgift'),(54,'Can delete events gift',18,'delete_eventsgift'),(55,'Can add gift descript',19,'add_giftdescript'),(56,'Can change gift descript',19,'change_giftdescript'),(57,'Can delete gift descript',19,'delete_giftdescript'),(58,'Can add gift outs',20,'add_giftouts'),(59,'Can change gift outs',20,'change_giftouts'),(60,'Can delete gift outs',20,'delete_giftouts'),(61,'Can add users',21,'add_users'),(62,'Can change users',21,'change_users'),(63,'Can delete users',21,'delete_users');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$100000$uIJzjfNnNCf0$eFryniepi0ljpHOqTsyHf2EHxp62Ap4fl3BgDJPlmcM=','2018-08-01 16:44:49.003650',1,'admin','','','gentaliana@gmail.com',1,1,'2018-07-23 15:23:13.211827'),(2,'pbkdf2_sha256$100000$1IrO1t0PM2Gb$tsOnhnopSIuxpbmASios+kQ7MOY8SIw/8BmD+p8UhB4=','2018-08-08 07:57:21.206611',1,'arcanar7','','','arcanar7@gmail.com',1,1,'2018-07-25 11:04:27.121884'),(3,'pbkdf2_sha256$100000$7sgVMSutF5R7$wVny00U6mwyJY/qu71mkTuLrKuQ56ym/X+V99VDb26A=','2018-07-26 16:14:26.000000',0,'user','U','test','gentaliana@gmail.com',0,1,'2018-07-26 15:55:56.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,3,1);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-07-23 15:39:36.533069','4','EventsDescript object (4)',2,'[{\"changed\": {\"fields\": [\"descript\"]}}]',17,1),(2,'2018-07-26 08:28:42.170665','3','EventsDescript object (3)',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',17,2),(3,'2018-07-26 15:55:57.169897','3','user',1,'[{\"added\": {}}]',4,1),(4,'2018-07-26 15:57:07.639995','3','user',2,'[{\"changed\": {\"fields\": [\"first_name\", \"last_name\", \"email\", \"user_permissions\", \"last_login\"]}}]',4,1),(5,'2018-07-26 15:57:56.330064','1','Бот',1,'[{\"added\": {}}]',3,1),(6,'2018-07-26 15:58:15.060090','3','user',2,'[{\"changed\": {\"fields\": [\"groups\"]}}]',4,1),(7,'2018-07-26 16:15:52.461570','3','user',2,'[{\"changed\": {\"fields\": [\"user_permissions\"]}}]',4,1),(8,'2018-07-28 15:43:22.124049','67','382685647',2,'[{\"changed\": {\"fields\": [\"status\"]}}]',20,2),(9,'2018-07-28 15:43:33.944725','66','382685647',2,'[{\"changed\": {\"fields\": [\"status\"]}}]',20,2),(10,'2018-07-28 15:47:21.396734','66','382685647',2,'[{\"changed\": {\"fields\": [\"status\"]}}]',20,2),(11,'2018-07-28 15:52:54.229771','66','382685647',2,'[{\"changed\": {\"fields\": [\"status\"]}}]',20,2),(12,'2018-07-28 15:57:57.045723','67','382685647',2,'[{\"changed\": {\"fields\": [\"status\"]}}]',20,1),(13,'2018-07-28 15:58:09.813453','66','382685647',2,'[{\"changed\": {\"fields\": [\"status\"]}}]',20,1),(14,'2018-07-28 16:00:09.222651','67','382685647',2,'[{\"changed\": {\"fields\": [\"status\"]}}]',20,2),(15,'2018-07-28 16:00:33.568044','66','382685647',2,'[{\"changed\": {\"fields\": [\"status\"]}}]',20,2),(16,'2018-07-29 14:32:00.909995','8','Подарок1',3,'',19,2),(17,'2018-07-29 15:02:47.181452','60','Users object (60)',1,'[{\"added\": {}}]',21,1),(18,'2018-07-29 15:17:22.995546','60','Users object (60)',3,'',21,1),(19,'2018-07-30 10:51:46.739312','67','382685647',2,'[{\"changed\": {\"fields\": [\"status\"]}}]',20,2),(20,'2018-07-30 10:51:58.441981','66','382685647',2,'[{\"changed\": {\"fields\": [\"status\"]}}]',20,2),(21,'2018-07-30 11:06:21.879367','67','382685647',2,'[{\"changed\": {\"fields\": [\"status\"]}}]',20,2),(22,'2018-07-30 11:06:35.538148','66','382685647',2,'[{\"changed\": {\"fields\": [\"status\"]}}]',20,2),(23,'2018-07-30 11:15:26.082494','66','382685647',2,'[{\"changed\": {\"fields\": [\"status\"]}}]',20,2),(24,'2018-07-30 11:26:17.755767','66','382685647',2,'[{\"changed\": {\"fields\": [\"status\"]}}]',20,2);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(7,'catalog','authgroup'),(8,'catalog','authgrouppermissions'),(9,'catalog','authpermission'),(10,'catalog','authuser'),(11,'catalog','authusergroups'),(12,'catalog','authuseruserpermissions'),(13,'catalog','djangoadminlog'),(14,'catalog','djangocontenttype'),(15,'catalog','djangomigrations'),(16,'catalog','djangosession'),(17,'catalog','eventsdescript'),(18,'catalog','eventsgift'),(19,'catalog','giftdescript'),(20,'catalog','giftouts'),(21,'catalog','users'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-07-23 15:21:15.194076'),(2,'auth','0001_initial','2018-07-23 15:21:19.874344'),(3,'admin','0001_initial','2018-07-23 15:21:21.266424'),(4,'admin','0002_logentry_remove_auto_add','2018-07-23 15:21:21.451434'),(5,'contenttypes','0002_remove_content_type_name','2018-07-23 15:21:21.844457'),(6,'auth','0002_alter_permission_name_max_length','2018-07-23 15:21:22.057469'),(7,'auth','0003_alter_user_email_max_length','2018-07-23 15:21:22.280482'),(8,'auth','0004_alter_user_username_opts','2018-07-23 15:21:22.461492'),(9,'auth','0005_alter_user_last_login_null','2018-07-23 15:21:22.680505'),(10,'auth','0006_require_contenttypes_0002','2018-07-23 15:21:22.849514'),(11,'auth','0007_alter_validators_add_error_messages','2018-07-23 15:21:23.030525'),(12,'auth','0008_alter_user_username_max_length','2018-07-23 15:21:23.252537'),(13,'auth','0009_alter_user_last_name_max_length','2018-07-23 15:21:23.474550'),(14,'catalog','0001_initial','2018-07-23 15:21:26.891745'),(15,'catalog','0002_auto_20180723_1819','2018-07-23 15:21:27.610787'),(16,'sessions','0001_initial','2018-07-23 15:21:28.268824'),(17,'catalog','0003_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissions_django','2018-07-23 15:36:13.444453');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('ddwe8xlpzlt0qnp764gfxkqpj8x80c04','MjU0NzYzNGE5Yjc4ZWZlZDU2OGNhMGVjM2ZkMDZkZjA5ZjA4NjVhYjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjOWEyYjBlNWZkMjdjMzM0NGE2YjMyYmE1YjhjYTliNGJkYjY2YWRmIn0=','2018-08-18 09:26:04.032518'),('qv2sr2asnzgqfaq81q9p4ma1c36dvemo','ZGY3YWIwMWUyM2M0MDcyYWJmMDkyYjI1NGY5ODEyMTk4NzM0YjAyOTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkZWEwMTAxNjkzOThjNDJiYWUxMzY3YTdlYzY4Y2QwMDA5YjQ0YzQwIn0=','2018-08-15 16:44:49.145658'),('vzrh6f9k7esw7lfsp1s96uslua29iljr','MjU0NzYzNGE5Yjc4ZWZlZDU2OGNhMGVjM2ZkMDZkZjA5ZjA4NjVhYjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjOWEyYjBlNWZkMjdjMzM0NGE2YjMyYmE1YjhjYTliNGJkYjY2YWRmIn0=','2018-08-22 07:57:21.505628');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `events_descript`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `events_descript` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(300) DEFAULT NULL,
  `descript` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events_descript`
--

LOCK TABLES `events_descript` WRITE;
/*!40000 ALTER TABLE `events_descript` DISABLE KEYS */;
INSERT INTO `events_descript` VALUES (1,'Добро пожаловать','За самостоятельный вход в систему'),(2,'Пригласил друга','За успешное приглашение друга'),(3,'Откликнулся на приглашение друга','Пришел на зов друзей'),(4,'С Днем Рождения','Поздравляем С Днем Рождения!!!'),(5,'Новое событие1','Описание события'),(6,'Привет','dfgdgdf'),(7,'блабла1','блаблабла');
/*!40000 ALTER TABLE `events_descript` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `events_gift`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `events_gift` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_event` int(11) DEFAULT NULL,
  `id_gift` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events_gift`
--

LOCK TABLES `events_gift` WRITE;
/*!40000 ALTER TABLE `events_gift` DISABLE KEYS */;
INSERT INTO `events_gift` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,2,2),(6,2,3),(7,2,4),(8,3,2),(9,3,3),(10,3,4),(11,4,5),(12,4,6),(13,4,7),(14,6,9),(15,6,10),(16,7,10),(17,5,4),(18,5,1);
/*!40000 ALTER TABLE `events_gift` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gift_descript`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gift_descript` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(300) DEFAULT NULL,
  `cnt` int(11) DEFAULT NULL,
  `img` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gift_descript`
--

LOCK TABLES `gift_descript` WRITE;
/*!40000 ALTER TABLE `gift_descript` DISABLE KEYS */;
INSERT INTO `gift_descript` VALUES (1,'Зонтик',21,'img1.jpg'),(2,'Код активации времени на компах',20,'img2.jpg'),(3,'Браслеты NEXT',21,'img2.jpg'),(4,'Часы NEXT',27,'img2.jpg'),(5,'Зона Studio',30,'img2.jpg'),(6,'Пеньята ',30,'img2.jpg'),(7,'Торт',30,'img2.jpg'),(9,'Подарок test',10,NULL),(10,'Подарок test2',11,NULL);
/*!40000 ALTER TABLE `gift_descript` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gift_outs`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gift_outs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_user` varchar(30) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `id_event_gift` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gift_outs`
--

LOCK TABLES `gift_outs` WRITE;
/*!40000 ALTER TABLE `gift_outs` DISABLE KEYS */;
INSERT INTO `gift_outs` VALUES (66,'382685647','Ожидает выдачи',3),(67,'382685647','Ожидает выдачи',4),(68,'382685647','Ожидает выдачи',1);
/*!40000 ALTER TABLE `gift_outs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt_add` datetime DEFAULT NULL,
  `id_user` varchar(30) DEFAULT NULL,
  `id_invite` varchar(300) DEFAULT NULL,
  `name` varchar(300) DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `dt_birth` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (58,'2018-07-25 14:36:24','382685647','382685647','test1','+79061680172','2000-01-01 00:00:00'),(59,'2018-07-27 11:32:31','382685647','382685647','test1','+79061680172','2000-01-01 00:00:00'),(61,'2018-08-03 14:38:19','272541442','272541442',NULL,NULL,NULL),(62,'2018-08-07 11:37:44','272541442','272541442',NULL,NULL,NULL),(63,'2018-08-07 11:59:04','382685647','382685647','test1','+79061680172','2000-01-01 00:00:00');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-08-08 13:14:20

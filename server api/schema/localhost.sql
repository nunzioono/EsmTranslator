-- phpMyAdmin SQL Dump
-- version 4.1.7
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Lug 03, 2022 alle 18:00
-- Versione del server: 8.0.26
-- PHP Version: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `my_nodev`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `translators`
--

CREATE TABLE IF NOT EXISTS `translators` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `api_key` varchar(255) NOT NULL,
  `consumption` int NOT NULL,
  `limit` int NOT NULL,
  `created_at` datetime NOT NULL,
  `last_update` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci AUTO_INCREMENT=1 ;

--
-- Dump dei dati per la tabella `translators`
--

INSERT INTO `translators` (`id`, `name`, `api_key`, `consumption`, `limit`, `created_at`, `last_update`) VALUES
(1, 'DeepL', 'ddc96844-754b-f50c-0b53-9dacdaf602ef:fx', 202992, 500000, '2022-06-27 17:54:00', '2022-07-03 17:54:04');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : dim. 31 mai 2026 à 08:38
-- Version du serveur : 8.2.0
-- Version de PHP : 8.2.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET FOREIGN_KEY_CHECKS=0;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `sae204_c5_bd`
--

-- --------------------------------------------------------

--
-- Structure de la table `departement`
--

DROP TABLE IF EXISTS `departement`;
CREATE TABLE IF NOT EXISTS `departement` (
  `id` int NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL,
  `libelle` varchar(100) NOT NULL,
  `region_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`),
  KEY `region_id` (`region_id`),
  CONSTRAINT `fk_departement_region` FOREIGN KEY (`region_id`) REFERENCES `region` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=102 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `departement`
--

INSERT INTO `departement` (`id`, `code`, `libelle`, `region_id`) VALUES
(1, '01', 'Ain', 16),
(2, '02', 'Aisne', 10),
(3, '03', 'Allier', 16),
(4, '04', 'Alpes-de-Haute-Provence', 17),
(5, '05', 'Hautes-Alpes', 17),
(6, '06', 'Alpes-Maritimes', 17),
(7, '07', 'Ardèche', 16),
(8, '08', 'Ardennes', 11),
(9, '09', 'Ariège', 15),
(10, '10', 'Aube', 11),
(11, '11', 'Aude', 15),
(12, '12', 'Aveyron', 15),
(13, '13', 'Bouches-du-Rhône', 17),
(14, '14', 'Calvados', 9),
(15, '15', 'Cantal', 16),
(16, '16', 'Charente', 14),
(17, '17', 'Charente-Maritime', 14),
(18, '18', 'Cher', 7),
(19, '19', 'Corrèze', 14),
(20, '21', 'Côte-dOr', 8),
(21, '22', 'Côtes-dArmor', 13),
(22, '23', 'Creuse', 14),
(23, '24', 'Dordogne', 14),
(24, '25', 'Doubs', 8),
(25, '26', 'Drôme', 16),
(26, '27', 'Eure', 9),
(27, '28', 'Eure-et-Loir', 7),
(28, '29', 'Finistère', 13),
(29, '2A', 'Corse-du-Sud', 18),
(30, '2B', 'Haute-Corse', 18),
(31, '30', 'Gard', 15),
(32, '31', 'Haute-Garonne', 15),
(33, '32', 'Gers', 15),
(34, '33', 'Gironde', 14),
(35, '34', 'Hérault', 15),
(36, '35', 'Ille-et-Vilaine', 13),
(37, '36', 'Indre', 7),
(38, '37', 'Indre-et-Loire', 7),
(39, '38', 'Isère', 16),
(40, '39', 'Jura', 8),
(41, '40', 'Landes', 14),
(42, '41', 'Loir-et-Cher', 7),
(43, '42', 'Loire', 16),
(44, '43', 'Haute-Loire', 16),
(45, '44', 'Loire-Atlantique', 12),
(46, '45', 'Loiret', 7),
(47, '46', 'Lot', 15),
(48, '47', 'Lot-et-Garonne', 14),
(49, '48', 'Lozère', 15),
(50, '49', 'Maine-et-Loire', 12),
(51, '50', 'Manche', 9),
(52, '51', 'Marne', 11),
(53, '52', 'Haute-Marne', 11),
(54, '53', 'Mayenne', 12),
(55, '54', 'Meurthe-et-Moselle', 11),
(56, '55', 'Meuse', 11),
(57, '56', 'Morbihan', 13),
(58, '57', 'Moselle', 11),
(59, '58', 'Nièvre', 8),
(60, '59', 'Nord', 10),
(61, '60', 'Oise', 10),
(62, '61', 'Orne', 9),
(63, '62', 'Pas-de-Calais', 10),
(64, '63', 'Puy-de-Dôme', 16),
(65, '64', 'Pyrénées-Atlantiques', 14),
(66, '65', 'Hautes-Pyrénées', 15),
(67, '66', 'Pyrénées-Orientales', 15),
(68, '67', 'Bas-Rhin', 11),
(69, '68', 'Haut-Rhin', 11),
(70, '69', 'Rhône', 16),
(71, '70', 'Haute-Saône', 8),
(72, '71', 'Saône-et-Loire', 8),
(73, '72', 'Sarthe', 12),
(74, '73', 'Savoie', 16),
(75, '74', 'Haute-Savoie', 16),
(76, '75', 'Paris', 6),
(77, '76', 'Seine-Maritime', 9),
(78, '77', 'Seine-et-Marne', 6),
(79, '78', 'Yvelines', 6),
(80, '79', 'Deux-Sèvres', 14),
(81, '80', 'Somme', 10),
(82, '81', 'Tarn', 15),
(83, '82', 'Tarn-et-Garonne', 15),
(84, '83', 'Var', 17),
(85, '84', 'Vaucluse', 17),
(86, '85', 'Vendée', 12),
(87, '86', 'Vienne', 14),
(88, '87', 'Haute-Vienne', 14),
(89, '88', 'Vosges', 11),
(90, '89', 'Yonne', 8),
(91, '90', 'Territoire de Belfort', 8),
(92, '91', 'Essonne', 6),
(93, '92', 'Hauts-de-Seine', 6),
(94, '93', 'Seine-Saint-Denis', 6),
(95, '94', 'Val-de-Marne', 6),
(96, '95', 'Val-dOise', 6),
(97, '971', 'Guadeloupe', 1),
(98, '972', 'Martinique', 2),
(99, '973', 'Guyane', 3),
(100, '974', 'La Réunion', 4),
(101, '976', 'Mayotte', 5);

-- --------------------------------------------------------

--
-- Structure de la table `profession_sante`
--

DROP TABLE IF EXISTS `profession_sante`;
CREATE TABLE IF NOT EXISTS `profession_sante` (
  `id` int NOT NULL AUTO_INCREMENT,
  `libelle` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `libelle` (`libelle`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `profession_sante`
--

INSERT INTO `profession_sante` (`id`, `libelle`) VALUES
(1, 'Allergologues'),
(2, 'Anesthésistes-réanimateurs'),
(3, 'Autres médecins'),
(4, 'Cardiologues'),
(5, 'Chirurgiens'),
(6, 'Chirurgiens-dentistes (hors spécialistes dorthopédie dento-faciale - ODF)'),
(7, 'Chirurgiens-dentistes spécialistes dorthopédie dento-faciale (ODF)'),
(8, 'Dermatologues'),
(9, 'Endocrinologues'),
(10, 'Ensemble des auxiliaires médicaux'),
(11, 'Ensemble des chirurgiens-dentistes'),
(12, 'Ensemble des médecins'),
(13, 'Ensemble des médecins généralistes'),
(14, 'Ensemble des médecins spécialistes (hors généralistes)'),
(15, 'Gynécologues médicaux et obstétriciens'),
(16, 'Hépato-gastro-entérologues'),
(17, 'Infirmiers'),
(18, 'Masseurs-kinésithérapeutes'),
(19, 'Médecins généralistes (hors médecins à expertise particulière - MEP)'),
(20, 'Médecins généralistes à expertise particulière (MEP)'),
(21, 'Médecins nucléaires'),
(22, 'Médecins pathologistes'),
(23, 'Médecins vasculaires'),
(24, 'Neurologues'),
(25, 'Néphrologues'),
(26, 'Ophtalmologues'),
(27, 'Orthophonistes'),
(28, 'Orthoptistes'),
(29, 'Oto-rhino-laryngologistes'),
(30, 'Pneumologues'),
(31, 'Psychiatres'),
(32, 'Pédiatres'),
(33, 'Pédicures-podologues'),
(34, 'Radiologues'),
(35, 'Radiothérapeutes'),
(36, 'Rhumatologues'),
(37, 'Sages-femmes'),
(38, 'Stomatologues');

-- --------------------------------------------------------

--
-- Structure de la table `region`
--

DROP TABLE IF EXISTS `region`;
CREATE TABLE IF NOT EXISTS `region` (
  `id` int NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL,
  `libelle` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `region`
--

INSERT INTO `region` (`id`, `code`, `libelle`) VALUES
(1, '01', 'Guadeloupe'),
(2, '02', 'Martinique'),
(3, '03', 'Guyane'),
(4, '04', 'La Réunion'),
(5, '06', 'Mayotte'),
(6, '11', 'Ile-de-France'),
(7, '24', 'Centre-Val de Loire'),
(8, '27', 'Bourgogne-Franche-Comté'),
(9, '28', 'Normandie'),
(10, '32', 'Hauts-de-France'),
(11, '44', 'Grand Est'),
(12, '52', 'Pays de la Loire'),
(13, '53', 'Bretagne'),
(14, '75', 'Nouvelle-Aquitaine'),
(15, '76', 'Occitanie'),
(16, '84', 'Auvergne-Rhône-Alpes'),
(17, '93', 'Provence-Alpes-Côte dAzur'),
(18, '94', 'Corse'),
(19, '99', 'FRANCE');

-- --------------------------------------------------------

--
-- Structure de la table `sexe`
--

DROP TABLE IF EXISTS `sexe`;
CREATE TABLE IF NOT EXISTS `sexe` (
  `id` int NOT NULL AUTO_INCREMENT,
  `libelle` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `libelle` (`libelle`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `sexe`
--

INSERT INTO `sexe` (`id`, `libelle`) VALUES
(1, 'femmes'),
(2, 'hommes'),
(3, 'sexe inconnu'),
(4, 'tout sexe');

-- --------------------------------------------------------

--
-- Structure de la table `tranche_age`
--

DROP TABLE IF EXISTS `tranche_age`;
CREATE TABLE IF NOT EXISTS `tranche_age` (
  `id` int NOT NULL AUTO_INCREMENT,
  `libelle` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `libelle` (`libelle`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `tranche_age`
--

INSERT INTO `tranche_age` (`id`, `libelle`) VALUES
(1, '70 ans et plus'),
(2, 'Tout âge'),
(3, 'de 25 à 29 ans'),
(4, 'de 30 à 34 ans'),
(5, 'de 35 à 39 ans'),
(6, 'de 40 à 44 ans'),
(7, 'de 45 à 49 ans'),
(8, 'de 50 à 54 ans'),
(9, 'de 55 à 59 ans'),
(10, 'de 60 à 64 ans'),
(11, 'de 65 à 69 ans'),
(12, 'moins de 25 ans'),
(13, 'âge inconnu');

-- --------------------------------------------------------

--
-- Structure de la table `type_exercice`
--

DROP TABLE IF EXISTS `type_exercice`;
CREATE TABLE IF NOT EXISTS `type_exercice` (
  `id` int NOT NULL AUTO_INCREMENT,
  `libelle` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `libelle` (`libelle`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `type_exercice`
--

INSERT INTO `type_exercice` (`id`, `libelle`) VALUES
(1, 'libéral exclusif'),
(2, 'libéral mixte');

-- --------------------------------------------------------

--
-- Structure de la table `type_honoraire`
--

DROP TABLE IF EXISTS `type_honoraire`;
CREATE TABLE IF NOT EXISTS `type_honoraire` (
  `id` int NOT NULL AUTO_INCREMENT,
  `niveau_1` varchar(80) NOT NULL,
  `niveau_2` varchar(80) DEFAULT NULL,
  `niveau_3` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `niveau_1` (`niveau_1`,`niveau_2`,`niveau_3`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `type_honoraire`
--

INSERT INTO `type_honoraire` (`id`, `niveau_1`, `niveau_2`, `niveau_3`) VALUES
(1, 'Honoraires', 'Sans depassement', 'Totaux'),
(2, 'Honoraires', 'Sans depassement', 'Moyens'),
(3, 'Honoraires', 'Depassements', 'Totaux'),
(4, 'Honoraires', 'Depassements', 'Moyens'),
(5, 'Taux', 'Depassement', NULL),
(6, 'Taux', 'Depassement S2', NULL),
(7, 'Taux', 'Depassement S2', 'OPTAM'),
(8, 'Taux', 'Depassement S2', 'Non OPTAM');

-- --------------------------------------------------------

--
-- Structure de la table `type_prescription`
--

DROP TABLE IF EXISTS `type_prescription`;
CREATE TABLE IF NOT EXISTS `type_prescription` (
  `id` int NOT NULL AUTO_INCREMENT,
  `libelle` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `libelle` (`libelle`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `type_prescription`
--

INSERT INTO `type_prescription` (`id`, `libelle`) VALUES
(1, 'autres'),
(2, 'biologie'),
(3, 'dispositifs médicaux inscrits à la liste des produits et prestations (LPP)'),
(4, 'indemnités journalières'),
(5, 'kinésithérapie'),
(6, 'médicaments'),
(7, 'soins infirmiers'),
(8, 'total postes de prescriptions'),
(9, 'transports des malades');

-- --------------------------------------------------------

--
-- Structure de la table `type_secteur`
--

DROP TABLE IF EXISTS `type_secteur`;
CREATE TABLE IF NOT EXISTS `type_secteur` (
  `id` int NOT NULL AUTO_INCREMENT,
  `code` varchar(20) NOT NULL,
  `libelle` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `type_secteur`
--

INSERT INTO `type_secteur` (`id`, `code`, `libelle`) VALUES
(1, 'S1', 'Secteur 1 - Honoraires opposables'),
(2, 'S2', 'Secteur 2 - Honoraires libres avec tact et mesure'),
(3, 'S2_OPTAM', 'Secteur 2 avec OPTAM (Option Pratique Tarifaire Maitrisee)'),
(4, 'NC', 'Non conventionne');
SET FOREIGN_KEY_CHECKS=1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

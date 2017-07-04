-- phpMyAdmin SQL Dump
-- version 4.2.7.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 01, 2016 at 05:01 
-- Server version: 5.6.20
-- PHP Version: 5.5.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `rumahsakit`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE IF NOT EXISTS `admin` (
  `username` varchar(10) NOT NULL,
  `password` varchar(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`username`, `password`) VALUES
('agnes', '827ccb0e'),
('budi', 'e10adc39');

-- --------------------------------------------------------

--
-- Table structure for table `pasien`
--

CREATE TABLE IF NOT EXISTS `pasien` (
  `id_pasien` int(3) NOT NULL,
  `nama` varchar(55) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `agama` varchar(15) NOT NULL,
  `BirthDate` varchar(2) NOT NULL,
  `BirthMonth` varchar(15) NOT NULL,
  `BirthYear` varchar(4) NOT NULL,
  `Email_id` varchar(30) NOT NULL,
  `tlp` varchar(12) NOT NULL,
  `alamat` varchar(60) NOT NULL,
  `darah` varchar(2) NOT NULL,
  `riwayat_penyakit` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pasien`
--

INSERT INTO `pasien` (`id_pasien`, `nama`, `gender`, `agama`, `BirthDate`, `BirthMonth`, `BirthYear`, `Email_id`, `tlp`, `alamat`, `darah`, `riwayat_penyakit`) VALUES
(1, 'agnes', 'Perempuan', 'Protestan', '26', '03', '1994', 'agnescexa@gmail', '082125356750', 'Jl. Flamboyan Raya H1 No.2', 'B', 'alergi, asma, flu, demam'),
(2, 'adul', 'Laki-Laki', 'Budha', '10', 'September', '1989', 'adul@yahoo.com', '08563737392', 'Surabaya', 'AB', 'alergi makanan'),
(3, 'abby', 'Laki-Laki', 'Hindu', '16', '09', '1999', 'ahahah@gmail.co', '0895858585', 'Jl. gunung semeru 1', 'AB', 'tidak ada'),
(4, 'Fina', 'Perempuan', 'Islam', '4', '04', '1993', 'finaaa@gmail.com', '082238849202', 'JL. Bendungan Sigura-gura', 'O', 'darah rendah, alergi makanan'),
(5, 'sfga', 'Laki-Laki', 'Hindu', '16', '10', '1998', 'ddkdk@mgmgm', '0659669696', 'JL. akakakaka', 'B', 'tidak ada');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
 ADD PRIMARY KEY (`password`);

--
-- Indexes for table `pasien`
--
ALTER TABLE `pasien`
 ADD PRIMARY KEY (`id_pasien`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

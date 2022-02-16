-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 16, 2022 at 03:17 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `student_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `roll_no` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `dob` varchar(100) NOT NULL,
  `address` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`roll_no`, `name`, `email`, `gender`, `contact`, `dob`, `address`) VALUES
(1, 'Riya', 'riya@gmail.com', 'Female', '1234567890', '1-1-2001', 'India\n'),
(2, 'Ruhan', 'ruhan@gmail.com', 'Male', '3214567809', '3-5-2001', 'India\n\n'),
(3, 'Rudra', 'rudra@gmail.com', 'Male', '9087654321', '9-10-2001', 'Mumbai\n'),
(4, 'Piyu', 'piyu@gmai.com', 'Female', '1234567890', '30-9-2001', 'pune\n'),
(5, 'jay', 'j1a2y3@gmail.com', 'Male', '9870654321', '8-3-2001', 'Mumbai\n'),
(6, 'piyu', 'piyu@gmail.com', 'Female', '4563728792', '5-9-2002', 'Madhay Pradesh\n\n'),
(7, 'Gauri', 'gauri@gmail.com', 'Female', '6785489032', '4-12-2001', 'Jalna\n'),
(8, 'Ganesh', 'ganesh@gmail.com', 'Male', '1234567890', '5-9-2001', 'Dhule\n'),
(9, 'Shree', 'shree@gmail.com', 'Male', '9807653241', '7-12-2001', 'Dhule\n'),
(10, 'Tina', 'tina@gmail.com', 'Female', '7864903652', '9-1-2001', 'Pachora\n');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`roll_no`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

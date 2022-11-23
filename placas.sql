-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-11-2022 a las 04:17:23
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `autos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `placas`
--

CREATE TABLE `placas` (
  `id_placa` int(11) NOT NULL,
  `placa` text NOT NULL,
  `Marca` text NOT NULL,
  `Modelo` text NOT NULL,
  `anio` int(11) DEFAULT NULL,
  `num_serie` text DEFAULT NULL,
  `color` text DEFAULT NULL,
  `num_puertas` int(11) DEFAULT NULL,
  `tipo_motor` text DEFAULT NULL,
  `nom_propietario` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `placas`
--

INSERT INTO `placas` (`id_placa`, `placa`, `Marca`, `Modelo`, `anio`, `num_serie`, `color`, `num_puertas`, `tipo_motor`, `nom_propietario`) VALUES
(1, 'GMXSP105', 'CHEVROLET', 'SPARK', 2006, 'RED152', 'azul', 4, '4 cilindros', 'Aquiles Caigo');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `placas`
--
ALTER TABLE `placas`
  ADD PRIMARY KEY (`id_placa`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `placas`
--
ALTER TABLE `placas`
  MODIFY `id_placa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

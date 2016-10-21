--
-- Database: `be_1`
--

-- --------------------------------------------------------

--
-- Table structure for table `links`
--

CREATE TABLE `links` (
  `link_id` int(11) NOT NULL,
  `page_id` int(11) NOT NULL,
  `link` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf32;

-- --------------------------------------------------------

--
-- Table structure for table `pages`
--

CREATE TABLE `pages` (
  `page_id` int(11) NOT NULL,
  `page_link` text NOT NULL,
  `page_title` text NOT NULL,
  `page_full_content` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf32;



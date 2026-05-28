CREATE DATABASE seismic_db;
USE seismic_db;
SELECT * FROM earthquakes LIMIT 5;
SELECT COUNT(*) FROM earthquakes;
SHOW TABLES;
DESCRIBE earthquakes;
UPDATE earthquakes
SET hour = HOUR(time);

UPDATE earthquakes
SET hour = HOUR(time);
ALTER TABLE earthquakes
ADD COLUMN continent VARCHAR(50),
ADD COLUMN casualties INT DEFAULT 0,
ADD COLUMN economic_loss DOUBLE DEFAULT 0;
UPDATE earthquakes
SET continent = 'North America'
WHERE place IN (
'9 km SE of York Harbor, Maine'
);
UPDATE earthquakes
SET continent = 'Asia'
WHERE country IN (
'Japan',
'Indonesia',
'Myanmar',
'China',
'India',
'Iran',
'Philippines',
'Taiwan',
'Banda Sea',
'Bhutan',
'Tajikistan-Xinjiang border',
'Afghanistan-Tajikistan border',
'Western Turkey',
'Turkey-Syria border',
'Madagascar',
'east of Severnaya Zemlaya',
'Thailand',
'Celebes Sea',
'Malaysia',
'Bay of Bengal',
'Timor Leste',
'Nepal',
'Pakistan',
'Afghanistan',
'Tajikistan',
'Kyrgyzstan',
'Mongolia',
'Chagos Archipelago',
'Yemen',
'Turkey',
'Central Turkey',
'western Xizang',
'Southern Tibetan Plateau',
'Kazakhstan',
'Saudi Arabia',
'Iraq',
'southern Iran',
'Syria',
'Bangladesh',
'eastern Turkey',
'Armenia',
'Ukraine',
'Turkmenistan',
'Philippine Islands',
'Russia region',
'Uzbekistan',
'north of Severnaya Zemlya',
'Burma (Myanmar)',
'Russia',
'Cyprus',
'Azerbaijan',
'Vietnam',
'Laos',
'Israel',
'western Iran',
'Northwestern Iran',
'Burma',
'Lebanon',
'Qatar',
'Kuwait',
'off the west coast of northern Sumatra',
'Oman',
'south of the Mariana Islands',
'Sea of Okhotsk',
'Fiji'
);
UPDATE earthquakes
SET continent = 'North America'
WHERE country IN (
'Alaska',
'CA',
'Honduras',
'Samoa Islands',
'Arizona',
'Colorado',
'Bermuda',
'Barbados',
'Beaufort Sea',
'MX',
'Gulf of America',
'near the coast of Venezuela',
'Illinois',
'Galapagos Triple Junction',
'north of Ascension Island',
'Virgin Islands',
'Dominican Republic',
'Guatemala',
'Molucca Sea',
'Mona Passage',
'Utah',
'off the coast of Central America',
'Montana',
'Nevada',
'Wyoming',
'U.S. Virgin Islands',
'Saint Lucia',
'Reykjanes Ridge',
'USA',
'Revilla Gigedo Islands',
'northern East Pacific Rise',
'Ascension Island',
'Washington',
'Minnesota',
'Ohio',
'Mexico',
'Antigua and barbuda',
'Cuba',
'Oregon',
'New York',
'New Jersey',
'Leeward Islands',
'Louisiana',
'off the coast of Oregon',
'off the coast of Washington',
'Canada',
'Jamaica',
'Trinidad and Tobago',
'Tennessee',
'South Carolina',
'near the coast of Guatemala',
'Panama',
'Idaho',
'central East Pacific Rise',
'southern East Pacific Rise',
'Nicaragua',
'Florida',
'Strait of Gibraltar',
'Dominica',
'Kansas',
'El Salvador',
'Prince Edward Islands',
'south of Panama',
'Texas',
'Anguilla',
'Cayman Islands',
'western Texas',
'Samoa',
'Puerto Rico'
);
UPDATE earthquakes
SET continent = 'South America'
WHERE country IN (
'Chile',
'Peru',
'Scotia Sea',
'South Georgia Island',
'southeast of Easter Island',
'Bolivia',
'west of the Galapagos Islands',
'Venezuela',
'Argentina',
'Falklands Islands',
'Ecuador'
);
UPDATE earthquakes
SET continent = 'Europe'
WHERE country IN (
'Greece',
'Greenland Sea',
'Switzerland',
'Saint Eustatius and Saba',
'Bulgaria',
'Hungary',
'North Macedonia',
'Azores Islands',
'Georgia',
'Norway',
'eastern Greenland',
'Austria',
'Kosovo',
'Southern Greece',
'Aegean Sea',
'Svalbard',
'north of Svalbard',
'Greenland',
'Spain',
'Bosnia and Herzegovina',
'Norwegian Sea',
'Croatia',
'Davis Strait',
'France',
'Poland',
'Svalbard and Jan Mayen',
'Italy',
'near the north coast of Greenland',
'Slovakia'
'Portugal',
'Mozambique Channel',
'Romania',
'Gernmany',
'central Mediterranean Sea',
'Arctic Ocean',
'Netherland',
'Adriatic Sea',
'Caspian Sea',
'Ionian Sea',
'eastern Mediterranean Sea',
'Portugal region',
'Serbia',
'United Kingdom',
'Iceland'
);
UPDATE earthquakes
SET continent = 'Africa'
WHERE country IN (
'Ethiopia',
'Angola',
'near the coast of Nicaragua',
'Gabon',
'Guinea',
'northern Algeria',
'near the coast of Libya',
'central Italy',
'Sudan',
'Morocco',
'Chad'
'Uganda',
'Algeria',
'Burundi',
'Montenegro',
'Mauritius',
'South Sudan',
'Kenya',
'Eritrea',
'Malta',
'Albania',
'Egypt',
'Namibia',
'South Africa',
'Mauritius - Reunion',
'Democratic Republic of the Congo',
'southwest of Africa',
'Somalia',
'Rwanda',
'Mozambique',
'Tunisia',
'Djibouti',
'Zambia',
'Malawi',
'Libya',
'Zimbabwe',
'Guyana',
'south of Africa',
'Costa Rica',
'Tanzania'
);
UPDATE earthquakes
SET continent = 'Australia'
WHERE country IN (
'New Zealand',
'Papua New Guinea',
'Macquarie Island',
'Australia'
);
UPDATE earthquakes
SET continent = 'Oceania'
WHERE country IN (
'Fiji',
'American Samoa',
'Micronesia',
'Bismarck Sea',
'Federated States of Micronesia',
'Palau',
'South Korea',
'Wallis and Futuna',
'Tonga',
'Haiti',
'Kiribati region',
'Kermadec Islands',
'Solomon Islands',
'Vanuatu',
'New Caledonia',
'Guam',
'west of Macquarie Island',
'Easter Island',
'Papua New Guinea',
'South Sandwich Islands'
);
UPDATE earthquakes
SET continent = 'Asia'
WHERE country IN (
'Kuril Islands',
'Kamchatka',
'Japan',
'Taiwan',
'Philippines',
'Indonesia',
'Mariana Islands'
);
UPDATE earthquakes
SET continent = 'North America'
WHERE country IN (
'Alaska',
'California',
'Santa Cruz Islands',
'9 km SE of York Harbor,Maine',
'Saint Helena',
'Oklahoma',
'Guadeloupe',
'Hawaii',
'Puerto Rico',
'Mexico',
'Aleutian Islands'
);
UPDATE earthquakes
SET continent = 'South America'
WHERE country IN (
'Chile',
'Peru',
'Brazil',
'Ecuador',
'Colombia'
);
UPDATE earthquakes
SET continent = 'Atlantic Ocean'
WHERE country IN (
'Mid-Atlantic Ridge',
'North Atlantic Ocean',
'Falkland Islands',
'Tristan da Cunha',
'Bouvet Island',
'South Atlantic Ocean',
'Drake Passage'
);
UPDATE earthquakes
SET continent = 'Indian Ocean'
WHERE country IN (
'southeast Indian Ridge',
'Indian Ocean',
'Owen Fracture Zone',
'Carlsberg Ridge'
);
UPDATE earthquakes
SET continent = 'Antarctica'
WHERE country IN (
'Southern Drake Passage',
'South Shetland Islands',
'Pacific-Antarctic Ridge',
'Balleny Islands',
'Antarctica'
);
UPDATE earthquakes
SET continent = 'Unknown'
WHERE continent IS NULL;
SELECT COUNT(*) AS unknown_count
FROM earthquakes
WHERE continent = 'Unknown';
SELECT country, COUNT(*) AS total
FROM earthquakes
WHERE continent = 'Unknown'
GROUP BY country
ORDER BY total DESC
LIMIT 100;
UPDATE earthquakes
SET continent = 'Asia'
WHERE country LIKE '%Japan%'
   OR country LIKE '%Indonesia%'
   OR country LIKE '%Philippines%'
   OR country LIKE '%China%'
   OR country LIKE '%Taiwan%'
   OR country LIKE '%Kuril%'
   OR country LIKE '%Kamchatka%'
   OR country LIKE '%India%'
   OR country LIKE '%Nepal%'
   OR country LIKE '%Pakistan%';
   UPDATE earthquakes
SET continent = 'North America'
WHERE country LIKE '%Alaska%'
   OR country LIKE '%California%'
   OR country LIKE '%Mexico%'
   OR country LIKE '%Puerto Rico%'
   OR country LIKE '%Hawaii%'
   OR country LIKE '%Aleutian%';
   UPDATE earthquakes
SET continent = 'South America'
WHERE country LIKE '%Chile%'
   OR country LIKE '%Peru%'
   OR country LIKE '%Ecuador%'
   OR country LIKE '%Argentina%'
   OR country LIKE '%Colombia%';
   UPDATE earthquakes
SET continent = 'Oceania'
WHERE country LIKE '%Fiji%'
OR country LIKE '%Northern Mariana Islands%'
OR country LIKE '%southeast of the Loyalty Islands%'
   OR country LIKE '%Tonga%'
   OR country LIKE '%Kermadec%'
   OR country LIKE '%Vanuatu%'
   OR country LIKE '%Solomon%'
   OR country LIKE '%Papua%'
   OR country LIKE '%New Zealand%';
   UPDATE earthquakes
SET continent = 'Atlantic Ocean'
WHERE country LIKE '%Atlantic%'
   OR country LIKE '%Drake Passage%'
   OR country LIKE '%east of the South Sandwich Islands%'
   OR country LIKE '%Mid-Atlantic%';
   UPDATE earthquakes
SET continent = 'Antarctica'
WHERE country LIKE '%Antarctica%'
   OR country LIKE '%Southern Drake%';
   SELECT COUNT(*) AS unknown_count
FROM earthquakes
WHERE continent = 'Unknown';
SELECT country, COUNT(*) AS total
FROM earthquakes
WHERE continent = 'Unknown'
GROUP BY country
ORDER BY total DESC
LIMIT 200;

UPDATE earthquakes
SET alert = 'unknown'
WHERE alert IS NULL;

UPDATE earthquakes
SET felt = 0
WHERE felt IS NULL;

SELECT alert, COUNT(*) AS total
FROM earthquakes
GROUP BY alert
ORDER BY total DESC;

ALTER TABLE earthquakes
DROP COLUMN economic_loss;
-- Casualty Estimation using felt column

UPDATE earthquakes
SET casualties = 0;
UPDATE earthquakes
SET casualties =
CASE

    -- Very dangerous earthquakes
    WHEN mag >= 8
         AND felt >= 20000
    THEN FLOOR(felt * 0.5)

    -- Strong populated earthquakes
    WHEN mag >= 7
         AND felt >= 10000
    THEN FLOOR(felt * 0.25)

    -- Moderate populated earthquakes
    WHEN mag >= 6
         AND felt >= 5000
    THEN FLOOR(felt * 0.2)

    -- Smaller impact
    WHEN felt >= 1000
    THEN FLOOR(felt * 0.15)

    ELSE 0

END;
SELECT
    place,
    continent,
    mag,
    felt,
    casualties
FROM earthquakes
ORDER BY casualties DESC
LIMIT 20
-- 



-- Creating tables (Normalized schemas)
CREATE TABLE countries (
	code VARCHAR(3) PRIMARY KEY,
	name VARCHAR(255)
);

CREATE TABLE unemployment_indicator (
	id INT PRIMARY KEY,
	country_code VARCHAR(3),
	year INT,
	value DOUBLE PRECISION,
	FOREIGN KEY (country_code) REFERENCES countries(code)
);

CREATE TABLE rural_pop_indicator (
	id INT PRIMARY KEY,
	country_code VARCHAR(3),
	year INT,
	value DOUBLE PRECISION,
	FOREIGN KEY (country_code) REFERENCES countries(code)
);

CREATE TABLE urban_pop_indicator (
	id INT PRIMARY KEY,
	country_code VARCHAR(3),
	year INT,
	value DOUBLE PRECISION,
	FOREIGN KEY (country_code) REFERENCES countries(code)
);

CREATE TABLE gdp_indicator (
	id INT PRIMARY KEY,
	country_code VARCHAR(3),
	year INT,
	value DOUBLE PRECISION,
	FOREIGN KEY (country_code) REFERENCES countries(code)
);

CREATE TABLE inflation_indicator (
	id INT PRIMARY KEY,
	country_code VARCHAR(3),
	year INT,
	value DOUBLE PRECISION,
	FOREIGN KEY (country_code) REFERENCES countries(code)
);

CREATE TABLE account_ownership_indicator (
	id INT PRIMARY KEY,
	country_code VARCHAR(3),
	year INT,
	value DOUBLE PRECISION,
	FOREIGN KEY (country_code) REFERENCES countries(code)
);

CREATE TABLE internet_indicator (
	id INT PRIMARY KEY,
	country_code VARCHAR(3),
	year INT,
	value DOUBLE PRECISION,
	FOREIGN KEY (country_code) REFERENCES countries(code)
);

CREATE TABLE mobile_indicator (
	id INT PRIMARY KEY,
	country_code VARCHAR(3),
	year INT,
	value DOUBLE PRECISION,
	FOREIGN KEY (country_code) REFERENCES countries(code)
);

CREATE TABLE personal_remit_indicator (
	id INT PRIMARY KEY,
	country_code VARCHAR(3),
	year INT,
	value DOUBLE PRECISION,
	FOREIGN KEY (country_code) REFERENCES countries(code)
);

CREATE TABLE pop_density_indicator (
	id INT PRIMARY KEY,
	country_code VARCHAR(3),
	year INT,
	value DOUBLE PRECISION,
	FOREIGN KEY (country_code) REFERENCES countries(code)
);

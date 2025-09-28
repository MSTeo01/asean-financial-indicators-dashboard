-- Create a table that holds the values for ten world bank indicators across ASEAN countries in the year 2012 - 2024
CREATE TABLE asean_2012_2024 (
    id INT PRIMARY KEY,
    country VARCHAR(255),
    country_code VARCHAR(3),
    year INT,
    unemployment_value DOUBLE PRECISION,
    inflation_value DOUBLE PRECISION,
    personal_remit_value DOUBLE PRECISION,
    mobile_value DOUBLE PRECISION,
    internet_value DOUBLE PRECISION,
    urb_pop_value DOUBLE PRECISION,
    rur_pop_value DOUBLE PRECISION,
    pop_density_value DOUBLE PRECISION,
    gdp_value DOUBLE PRECISION,
    acc_ownership_value DOUBLE PRECISION
)
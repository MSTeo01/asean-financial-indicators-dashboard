import world_bank_data as wb
import pandas as pd
import functools as ft
import sqlite3
import os


# Ten World Bank Indicators as metrics for the dashboard 
'''
Unemployment, Inflation, Personal Remittance, Mobile Subscriptions, Internet Usage,
Urban Population, Rural Population, Population Density, GDP, Financial Account Ownership
'''
indicators = ["SL.UEM.TOTL.ZS", "FP.CPI.TOTL.ZG", "BX.TRF.PWKR.CD.DT", "IT.CEL.SETS.P2", "IT.NET.USER.ZS", "SP.URB.TOTL.IN.ZS", "SP.RUR.TOTL.ZS", "EN.POP.DNST", "NY.GDP.PCAP.CD", "FX.OWN.TOTL.ZS"]
name = ["unemployment", "inflation", "personal_remit", "mobile", "internet", "urb_pop", "rur_pop", "pop_density", "gdp", "acc_ownership"]
current_directory = os.getcwd()
data_folder= current_directory + "/data"

# Get the indicator data from World Bank module (takes it directly from the API)
def get_indicator_data(tickers):
    data_lst = []
    ticker_count = 0
    
    # Create data folder
    os.makedirs(data_folder, exist_ok = True)
    path = data_folder + "/"

    for t in tickers:
        try:
            # Get the data for the years 2012 to 2024
            df = wb.get_series(t, date = '2012:2024').reset_index()

            # Put the data file into the data folder
            df.to_csv(path + name[ticker_count] + ".csv", index = False)

            data_lst.append(path + name[ticker_count] + ".csv")
            ticker_count += 1
        except Exception as err:
            print("Failed to get data for: ", t)
            print("Error: ", err)
    
    return data_lst

# Clean the data for each indicator file
def transform_data(file, index):
    df = pd.read_csv(file)

    # Filter for ASEAN countries
    asean = ['Brunei', 'Cambodia', 'Indonesia',
		     'Laos', 'Malaysia', 'Myanmar',
		     'Philippines', 'Singapore', 'Thailand',
		     'Vietnam']
    
    asean_countries_df = df[df['Country'].isin(asean)].reset_index(drop = True)

    # Mapping each country to three-letter codes
    country_code = {'Brunei':'BRN', 'Cambodia':'KHM', 'Indonesia':'IDN',
                    'Laos':'LAO', 'Malaysia':'MYS', 'Myanmar':'MMR',
                    'Phillippines':'PHL', 'Singapore':'SGP', 'Thailand':'THA',
                    'Vietnam':'VNM'}
    
    asean_countries_df['country_code'] = asean_countries_df['Country'].map(country_code)

    # Dropping Series column (name of the indicator) and renaming the indicator code with its name
    asean_countries_df = asean_countries_df.rename(columns = {indicators[index] : name[index] + "_value"})
    asean_countries_df = asean_countries_df.drop(columns = ["Series"])
    asean_countries_df = asean_countries_df.fillna(0)
    
    return asean_countries_df

# Merging all of the dataframes to consolidate all of the data in one big fact table
def merge_dfs(csv_files):
    df_final = ft.reduce(lambda left, right: pd.merge(left, right, on = ['Country', 'Year'], suffixes = ('', '_drop')), csv_files)
    df_final = df_final[[c for c in df_final.columns if not c.endswith('_drop')]]
    df_final['id'] = df_final.index
    
    cols_to_move = ['id', 'Country', 'country_code', 'Year']
    df_final = df_final[ cols_to_move + [ col for col in df_final.columns if col not in cols_to_move ] ]
    return df_final

# Save transformed data to SQLite database
def load_data(df, db_name = 'asean_world_bank_indicators.db', table_name = 'asean_2012_2024'):

    # Connect to SQLite database (creates if doesn't exist)
    conn = sqlite3.connect(db_name)

    try:
        df.to_sql(table_name, conn, if_exists = 'replace', index = False)

        # Verify the load was successful
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        record_count = cursor.fetchone()[0]
        
        print(f"Successfully loaded {record_count} records to '{table_name}' table")

        # Show a sample of what was loaded
        print("\nSample of loaded data:")
        sample_df = pd.read_sql_query(f"SELECT * FROM {table_name} LIMIT 5", conn)
        print(sample_df.to_string(index=False))
        
        return f"Data successfully loaded to {db_name}"

    except Exception as e:
        print(f"Error loading data: {e}")
        return None
    
    finally:
        conn.close()


def run_etl_pipeline():
    
    # Extract
    data = get_indicator_data(indicators)

    # Transform
    data_lst = []
    for index, file_name in enumerate(data):
        data_lst.append(transform_data(file_name, index))
    
    df = merge_dfs(data_lst)

    # Load
    load_data(df)

    return df


if __name__ == '__main__':
    run_etl_pipeline()
    

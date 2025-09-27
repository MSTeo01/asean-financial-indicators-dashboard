import world_bank_data as wb
import pandas as pd


# Ten World Bank Indicators as metrics for the dashboard 
'''
Unemployment, Inflation, Personal Remittance, Mobile Subscriptions, Internet Usage,
Urban Population, Rural Population, Population Density, GDP, Financial account ownership
'''
indicators = ['SL.UEM.TOTL.ZS', 'FP.CPI.TOTL.ZG', 'BX.TRF.PWKR.CD.DT', 'IT.CEL.SETS.P2', 'IT.NET.USER.ZS', 'SP.URB.TOTL.IN.ZS', 'SP.RUR.TOTL.ZS', 'EN.POP.DNST', 'NY.GDP.PCAP.CD', 'FX.OWN.TOTL.ZS']

# Get the indicator data from World Bank module (takes it directly from the API)
def get_indicator_data(tickers):
    data_lst = []
    for t in tickers:
        try:
            # Get the data for the years 2012 to 2024
            df = wb.get_series(t, date = '2012:2024').reset_index()
            data_lst.append(df)
        except Exception as err:
            print("Failed to get data for: ", t)
            print("Error: ", err)
    
    return data_lst

def transform_data():
    ...

def load_data():
    ...

# # Process...
# def process_indicator_csv(file):
#     df = pd.read_csv(file, skiprows = 4)
#     df = df.drop(['Indicator Name', 'Country Name', 'Indicator Code', 'Unnamed: 69'], axis = 1)
#     melted_df = df.melt(id_vars = ['Country Code'])
#     melted_df = melted_df.reset_index()
#     melted_df.rename(columns = {'index' : 'id', 'variable' : 'year'}, inplace = True)
#     melted_df.to_csv(file[:-4] + '_unpivot.csv', index = False)
#     return melted_df

# def get_country_name_code(file):
#     country_df = pd.read_csv(file, skiprows = 4)
#     country_df = country_df[['Country Code', 'Country Name']]
#     return 

# file_names = ['unemployment.csv', 'urb_pop.csv', 'rur_pop.csv', 'pop_density.csv', 'personal_remit.csv', 'mobile.csv', 
#               'internet.csv', 'inflation.csv', 'gdp.csv', 'acc_ownership.csv']

# df_lst = []
# for wbi in file_names:
#     world_bank = process_indicator_csv(wbi)
#     df_lst.append(world_bank)
# df_lst

if __name__ == '__main__':
    data = get_indicator_data(indicators)
    print(data[0])
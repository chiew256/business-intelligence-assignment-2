import pandas as pd

# Input
df = pd.read_csv('./input/FAOSTAT_data_en_12-28-2023.csv')

# Rename column
df.rename(columns={'Area': 'Country'}, inplace=True)

# Filtering
df_clean = df[~df['Flag'].isin(['O', 'M'])]

# Grouping and calculate average value for all months within each year for each country and element
df_clean = df_clean.groupby(['Country', 'Year', 'Element'], as_index=False)['Value'].mean()

# Output
df_clean.to_csv('./output/cleaned_FAOSTAT_data_en_12-28-2023.csv', index=False)

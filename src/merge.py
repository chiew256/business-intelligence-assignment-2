import pandas as pd

# Input
df_co2 = pd.read_csv('./output/cleaned_GCB2023v28_MtCO2_flat.csv')
df_faostat = pd.read_csv('./output/cleaned_FAOSTAT_data_en_12-28-2023.csv')

# Merge
df_merged = pd.merge(df_co2, df_faostat, on=['Country', 'Year'])

# Output
df_merged.to_csv('./output/merged.csv', index=False)

import pandas as pd

# Input
df = pd.read_csv('./input/GCB2023v28_MtCO2_flat.csv')

# Filtering
df = df.fillna(0)
df_clean = df[df['Total'] != 0]

# Output
df_clean.to_csv('./output/cleaned_GCB2023v28_MtCO2_flat.csv', index=False)

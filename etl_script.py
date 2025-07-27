import pandas as pd
import sqlite3
import os

# Create folders if not exist
os.makedirs('data', exist_ok=True)
os.makedirs('database', exist_ok=True)

# Sample CSV data
csv_file = 'data/sales_data.csv'
if not os.path.exists(csv_file):
    df_sample = pd.DataFrame({
        'OrderID': [1, 2, 3],
        'Customer': ['Alice', 'Bob', 'Charlie'],
        'Amount': [250, 150, 300]
    })
    df_sample.to_csv(csv_file, index=False)

# Extract
df = pd.read_csv(csv_file)
print("Extracted Data:")
print(df)

# Transform
df['AmountWithTax'] = df['Amount'] * 1.18

# Load
conn = sqlite3.connect('database/sales.db')
df.to_sql('sales', conn, if_exists='replace', index=False)
print("Data loaded to database.")

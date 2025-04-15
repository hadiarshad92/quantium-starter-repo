import pandas as pd
import glob

#load all csv files from the data directory
all_files = glob.glob("data/*.csv")

# create an empty list to store DataFrames
dfs = []

# loop through the list of files and read each one into a DataFrame
for filename in all_files:
    df = pd.read_csv(filename)
    # Append the DataFrame to the list
    dfs.append(df)
# concatenate all DataFrames in the list into a single DataFrame
df = pd.concat(dfs, ignore_index=True)

#filter for "pink morsel" only (case in-sensitive)
filtered_df = df[df['product'].str.lower() == 'pink morsel']

#convert price to float
filtered_df['price'] = filtered_df['price'].str.replace('[$,]', '', regex=True).astype(float)

#create new sales column
filtered_df['sales'] = filtered_df['price'] * filtered_df['quantity']

# # Step 5: Group by 'date' and 'region' and sum the sales
grouped = filtered_df.groupby(['date', 'region'], as_index=False)['sales'].sum()

#keep only 3 columns sales, date and region
final_df = grouped[['sales', 'date', 'region']]

#save to a new csv file
final_df.to_csv('formatted_sales.csv', index=False)




# import pandas as pd
# import glob

# # Step 1: Load all CSV files
# file_paths = glob.glob("data/daily_sales_*.csv")
# dfs = [pd.read_csv(file) for file in file_paths]

# # Step 2: Concatenate into a single DataFrame
# df = pd.concat(dfs, ignore_index=True)

# # Step 3: Filter only "pink morsel" rows (case-insensitive)
# df = df[df['product'].str.lower() == 'pink morsel']

# #convert price to float
# df['price'] = df['price'].str.replace('[$,]', '', regex=True).astype(float)

# # Step 4: Calculate the 'sales' column
# df['sales'] = df['quantity'] * df['price']

# # Step 5: Group by 'date' and 'region' and sum the sales
# grouped = df.groupby(['date', 'region'], as_index=False)['sales'].sum()

# # Step 6: Reorder columns to match required output
# grouped = grouped[['sales', 'date', 'region']]

# # Step 7: Save to CSV
# grouped.to_csv('formatted_sales.csv', index=False)

# print("✅ Done! Output saved as 'formatted_sales.csv'")


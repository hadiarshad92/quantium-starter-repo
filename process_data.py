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

#create new sales column
filtered_df['sales'] = filtered_df['price'] * filtered_df['quantity']

#keep only 3 columns sales, date and region
final_df = filtered_df[['sales', 'date', 'region']]

#save to a new csv file
final_df.to_csv('data/formatted_sales.csv', index=False)
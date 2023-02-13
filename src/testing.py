import pandas as pd

data = pd.read_csv("/Users/suvam/Documents/Text_processing_project/csv_data_cleaned/guess_max_freq.csv")
data.drop(columns=['Language','Mapped name'], inplace = True)
print(data.head(2))


guess_list = data['Guess'].unique()
n_guess = len(guess_list)
print(f"Number of unique guesses : {n_guess}, total number of names = {len(data)}")

print(data[10:20])

mask = data['Raw name'].str.contains("alterx ")
print(sum(mask))
res = data[mask]
import pprint
pprint.pprint(res[['Raw name','Guess']])


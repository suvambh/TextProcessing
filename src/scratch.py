import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('../csv_data_cleaned/normalised2.csv')
data = data.drop(columns=['Mapped name', 'Language',])
data.reset_index()
print(f"Program Start : Length of data = {len(data)}")
print(f"\n Data Head : {data.head(2)}, Data Index = {data.index}, Columns = {data.columns} ")
# sample dataframe of names
df = data
# convert the names to a list of words

words = []
appears_at = []
for name in df['Raw name'].index:
    for word in df.loc[name, 'Raw name'].split():
        words.append(word)
        appears_at.append(name)

# create a dataframe of the words and their indices
word_df = pd.DataFrame({'Word': words, 'Appearances': appears_at,
                        'Frequency': np.zeros(len(words)), 'Is_Number': np.zeros(len(words))})

# convert the index positions to a list for each word
word_df = word_df.groupby(['Word'])['Appearances'].apply(list).reset_index()

# count the frequency of each word and add it to the dataframe
word_df['Frequency'] = word_df["Appearances"].apply(lambda x: len(x))

check_type = lambda x: 1 if x.isdigit() else 0
word_df['Is_Number'] = word_df["Word"].apply(check_type)


print(f"The dataframe : {df} \n Frequency Pivot Table :\n {word_df.head(2)} \n Size : {word_df.shape}")
print(f"\n Examples \n: {word_df[30:40]}")

# is a3 a substring of a word? For example : xyza3pqr and a3. frequency of a3 ? 1 or 2.
# Write a function to obtain a dataframe, with input "word" and dataframe word_df and dataframe df.
# Use Boolean mask to get value (a list of numbers) from word_df["Appearances"] column when "word" == word_df["Word"]
# The value thus obtained is a list of indexes for the dataframe df where the "word" appear.
# Return the rows that have "word" in it else return empty dataframe.

import pandas as pd

def name_from_df(word, word_df, df):
    mask = word_df["Word"] == word
    index_list = word_df.loc[mask, "Appearances"].values
    if len(index_list) == 0:
        return pd.DataFrame()
    else:
        return df.loc[index_list[0]]


def create_tag_df(word_df):
    # Select words with frequency = 1
    tag_df = word_df[word_df["Frequency"] == 1]['Word'].copy()

    # Create a new column "tag" with the same data as the first column


    return tag_df

tag_df = pd.DataFrame(create_tag_df(word_df))
tag_df['Tag'] = None

sort_names = tag_df.sort_values(by='Word', key=lambda col: col.str.len())

print(f"\n tag_df columns = {tag_df.columns}:  \n{tag_df.head(30)}"
      f"\n Sorted Hear : \n {sort_names[500:530]}"
      f"\n Tail \n {sort_names.tail(1)}")

#word_lengths = sort_names['Word'].apply(lambda col: len(col))



def plot_word_lengths_histogram(words):
    # Get the length of each string in the series
    word_lengths = words.str.len()

    # Plot a histogram of the word lengths
    word_lengths.plot.hist(bins=range(word_lengths.min(), word_lengths.max() + 1), rwidth=0.9)

    # Add labels and title to the plot
    plt.xlabel('Word Length')
    plt.ylabel('Frequency')
    plt.title('Histogram of Word Lengths')

    # Show the plot
    plt.show()
plot_word_lengths_histogram(word_df['Word'])


#names = data['Raw name']
#print(names.head(20))
def remove_short_names(names):
    # Remove words with length 1
    names = names[names.str.len() > 1]
    # Remove words with length 2 that consist of only digits

    names = names[~(names.str.len() == 2 & names.str.isnumeric())]
    return names
#names = remove_short_names(names)
#print(names.head(20))


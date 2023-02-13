import pandas as pd
from collections import defaultdict

def probabilistically_guess_company(name, df, word_df, threshold=0.5):
    """Return a probable company name based on word frequency"""
    # Get the list of words in the name
    words = name.split()
    # Create a dictionary to store the frequency of each company name
    frequency = defaultdict(int)

    # Loop through each word in the list
    for word in words:
        word_row = word_df.loc[word_df['word'] == word]
        if word_row.empty:
            continue
        print(word_row['Appearances'])
        company_indices = word_row['Appearances']
        for index in company_indices:
            #print(word_row['frequency'].index)
            #print("name", df['Raw name'].to_list()[0])
            frequency[df.iloc[index]['Raw name'].to_list()[0]] += word_row.iloc[0]['frequency']

    # Normalize the frequency values
    total_frequency = sum(frequency.values())
    for key in frequency:
        frequency[key] /= total_frequency
    # Get the most probable company name based on frequency
    most_probable = max(frequency, key=frequency.get)
    return most_probable

df = pd.DataFrame({'Raw name': ['Alteryx', 'Alteryx Inc', 'Altran Innovación S.L.', 'Altran Innovacion Sociedad Limitada', 'Altran', 'Amicale Des Anciens Du Stade', 'Amicale Jean Baptiste Salis']})
word_df = pd.DataFrame({'word': ['Alteryx', 'Altran', 'Innovación', 'Sociedad', 'Limitada', 'Anciens', 'Stade', 'Jean', 'Baptiste', 'Salis'],
                       'Appearances': [[0, 1], [2, 3, 4], [2], [3], [3], [5], [5], [6], [6], [6]],
                       'frequency': [2, 3, 1, 1, 1, 1, 1, 1, 1, 1]})
input_name = 'Altran Innovación S.L.'
print(probabilistically_guess_company(input_name, df, word_df, threshold=0.))
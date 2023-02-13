import pprint

import pandas as pd
from collections import defaultdict

class GuessByFrequency:
    def __init__(self, name, df, word_df, threshold=0.5):
        self.name = name
        self.df = df
        self.word_df = word_df
        self.threshold = threshold

    def probabilistically_guess_company(self):
        """Return a probable company name based on word frequency"""
        # Get the list of words in the name
        words = self.name.split()
        # Create a dictionary to store the frequency of each company name
        frequency = defaultdict(int)

        # Loop through each word in the list
        for word in words:
            word_row = self.word_df.loc[self.word_df['Word'] == word]
            if word_row.empty:
                continue
            company_indices = word_row['Appearances']
            for index in company_indices:
                select_name_with_index = self.df.iloc[index]['Raw name'].to_list()[0]
                add_to_frequency = word_row.iloc[0]['Frequency']
                frequency[select_name_with_index] += add_to_frequency

        # Normalize the frequency values
        total_frequency = sum(frequency.values())
        for key in frequency:
            frequency[key] /= total_frequency
        # Get the most probable company name based on frequency
        most_probable = max(frequency, key=frequency.get)
        return most_probable

    def predict_companies(self):
        """Return a list of probable company names for each name in df"""
        results = []
        for index, row in self.df.iterrows():
            name = row['Raw name']
            guesser = GuessByFrequency(name, self.df, self.word_df)
            results.append(guesser.probabilistically_guess_company())
        return results

    def store_guess(self):
        """Create a new column in self.df called "Guess" and store the results of predict_companies"""
        results = self.predict_companies()
        self.df['Guess'] = results

    def guess_get_df(self):
        self.store_guess()
        return self.df


if __name__ == '__main__':

    df = pd.DataFrame({'Raw name': ['Alteryx', 'Alteryx Inc', 'Altran Innovación S.L.', 'Altran Innovacion Sociedad Limitada', 'Altran', 'Amicale Des Anciens Du Stade', 'Amicale Jean Baptiste Salis']})
    word_df = pd.DataFrame({'Word': ['Alteryx', 'Altran', 'Innovación', 'Sociedad', 'Limitada', 'Anciens', 'Stade', 'Jean', 'Baptiste', 'Salis'],
                       'Appearances': [[0, 1], [2, 3, 4], [2], [3], [3], [5], [5], [6], [6], [6]],
                       'Frequency': [2, 3, 1, 1, 1, 1, 1, 1, 1, 1]})
    input_name = 'Altran Innovación S.L.'

    obj = GuessByFrequency(input_name, df, word_df, threshold=0.)
    print(obj.probabilistically_guess_company())
    print(obj.guess_get_df())
    #pprint.pprint(word_df)
import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz
from collections import defaultdict

class GuessFromName:
    def __init__(self, name, df, words_df, p=0, q=-1, a=1, b=1):
        """
        Initializes a new instance of the GuessFromName class.

        Args:
            name (str): The name to guess from.
            df (pandas.DataFrame): The data frame containing company names.
            words_df (pandas.DataFrame): The data frame containing word frequencies.
            :parameter
            p (int): fuzz ratio with coefficient a (int) raised to the power of p.
            q (int): fuzz ratio with coefficient a (int) raised to the power of p.
            This is used to play with the model.

        """
        self.name = name
        self.df = df
        self.df['Score'] = np.zeros(len(df))
        self.words_df = words_df

        # Parameters
        self.p = p
        self.q = q
        self.a = a
        self.b = b

    def fuzzy_frequency_guess(self):
        """
        Returns the most probable company name based on word frequency and fuzziness score.

        Returns:
            (str, float): A tuple containing the name and score of the most probable company.
        """
        # Get the list of words in the name
        words = self.name.split()
        # Create a dictionary to store the score of each company name
        score = defaultdict(int)

        # Loop through each word in the list
        for word in words:
            mask = self.words_df['Word'] == word
            word_row = self.words_df[mask]
            if word_row.empty:
                continue
            company_indices = word_row['Appearances']
            for index in company_indices:
                select_name_with_index = self.df.iloc[index]['Raw name'].to_list()[0]
                add_to_frequency = word_row.iloc[0]['Frequency']
                fuzz_score = fuzz.token_sort_ratio(self.name, select_name_with_index)/100 # to normalize the range

                #The score is computed using a weighted sum of fuzzy matching scores and frequency of words in the company name,
                # where the weights are controlled by parameters a, b, p, and q. p and q should be of opposite sign.
                score[select_name_with_index] += (add_to_frequency)*(self.a*(fuzz_score)**(self.p)
                                                                     +self.b*(fuzz_score)**(self.q))

        # Normalize the score values
        total_score = sum(score.values())
        for key in score:
            score[key] /= total_score

        # Get the most probable company name based on frequency and score
        try :
            max_score_name = max(score, key=score.get)
            max_score = score[max_score_name]
        except:
            # For cases when company name has only high frequency words in its name
            max_score_name = self.name
            max_score = 1

        return max_score_name, max_score

    def predict_companies_from_df(self):
        """
        Returns a list of probable company names and scores for each name in df.
        """
        guessed_name = []
        guess_score = []
        for index, row in self.df.iterrows():
            name = row['Raw name']
            guesser = GuessFromName(name, self.df, self.words_df)
            guessed_name.append(guesser.fuzzy_frequency_guess()[0])
            guess_score.append(guesser.fuzzy_frequency_guess()[1])

        self.df['Mapped name'] = guessed_name
        self.df['Score'] = guess_score


    def guess_df(self):
        self.predict_companies_from_df()
        return self.df


if __name__ == '__main__':

    df = pd.DataFrame({'Raw name': ['Alteryx', 'Alteryx Inc', 'Altran Innovación S.L.', 'Altran Innovacion Sociedad Limitada', 'Altran', 'Amicale Des Anciens Du Stade', 'Amicale Jean Baptiste Salis']})
    word_df = pd.DataFrame({'Word': ['Alteryx', 'Altran', 'Innovación', 'Sociedad', 'Limitada', 'Anciens', 'Stade', 'Jean', 'Baptiste', 'Salis'],
                       'Appearances': [[0, 1], [2, 3, 4], [2], [3], [3], [5], [5], [6], [6], [6]],
                       'Frequency': [2, 3, 1, 1, 1, 1, 1, 1, 1, 1]})
    input_name = 'Altran Innovación S.L.'

    obj = GuessFromName(input_name, df, word_df)
    print(obj.fuzzy_frequency_guess())
    print(obj.guess_df())
    #pprint.pprint(word_df)
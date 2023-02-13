import pandas as pd
import numpy as np

class DataToMap:
    def __init__(self, df, column_name):
        self.df = df
        self.column_name = column_name
        self.words = []
        self.appears_at = []

    def map_data(self):
        for name in self.df[self.column_name].index:
            for word in self.df.loc[name, self.column_name].split():
                self.words.append(word)
                self.appears_at.append(name)

        return self.words, self.appears_at

    def create_word_df(self, words, appears_at):
        self.word_df = pd.DataFrame({'Word': words, 'Appearances': appears_at,
                                     'Frequency': np.zeros(len(words)), 'Is_Number': np.zeros(len(words))})
        return self.word_df

    def group_word_df(self):
        self.word_df = self.word_df.groupby(['Word'])['Appearances'].apply(list).reset_index()
        return self.word_df

    def count_frequency(self):
        self.word_df['Frequency'] = self.word_df["Appearances"].apply(lambda x: len(x))
        return self.word_df

    def search(self, word):
        mask = self.word_df["Word"] == word
        index_list = self.word_df.loc[mask, "Appearances"].values
        if len(index_list) == 0:
            return pd.DataFrame()
        else:
            return self.df.loc[index_list[0]]

    def add_is_number_column(self):
        def check_type(x):
            return 1 if x.isdigit() else 0

        self.word_df['Is_Number'] = self.word_df["Word"].apply(check_type)
        return self.word_df

    def describe_df(self, n1=0, n2=20):
        print(f"The dataframe :\n {self.word_df}")
        print(f"\nFirst 2 rows of the dataframe :\n {self.word_df.head(2)}")
        print(f"\nSize of the dataframe : {self.word_df.shape}")
        print(f"\nExamples from rows n1 to n2:\n {self.word_df[n1:n2]}")







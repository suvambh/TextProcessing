import pandas as pd
import numpy as np
import configparser

class DataToMap:
    def __init__(self, df):
        self.df = df
        self.col = df.columns[0]
        self.words = []  # empty list to store all the words found in the input data
        self.appears_at = []  # empty list to store the index of the input data where the corresponding word is found
        self.words_df = []  # empty dataframe to store the unique words along with their frequency of occurrence

        config = configparser.ConfigParser()
        config.read('../settings/config.ini')
        words_to_drop = config['file_paths']['words_to_drop']  # read the list of words to drop from the config file


    def map_data(self):
        """
        Extract all the words from the input data and their corresponding index where they appear
        :return: a tuple of two lists - words and appears_at
        """
        for name in self.df[self.col].index:
            for word in self.df.loc[name, self.col].split():
                self.words.append(word)
                self.appears_at.append(name)

        return self.words, self.appears_at


    def create_words_df(self, words, appears_at):
        """
        Create a dataframe with unique words and their frequency of occurrence
        :param words: list of all the words in the input data
        :param appears_at: list of indices where each corresponding word appears in the input data
        :return: words_df - a dataframe with unique words and their frequency of occurrence
        """
        self.words_df = pd.DataFrame({'Word': words, 'Appearances': appears_at,
                                     'Frequency': np.zeros(len(words))})
        return self.words_df


    def group_words_df(self):
        """
        Group words in the dataframe based on their value and create a list of indices where the word appears
        :return: a dataframe with unique words and the list of indices where they appear
        """
        self.words_df = self.words_df.groupby(['Word'])['Appearances'].apply(list).reset_index()
        return self.words_df


    def count_frequency(self):
        """
        Count the frequency of each word in the input data
        :return: a dataframe with unique words and their frequency of occurrence
        """
        self.words_df['Frequency'] = self.words_df["Appearances"].apply(lambda x: len(x))
        return self.words_df


    def search(self, word):
        """
        Search for a word in the dataframe and return the corresponding rows from the input data
        :param word: the word to search for
        :return: a dataframe with all rows where the word appears
        """
        mask = self.words_df["Word"] == word
        index_list = self.words_df.loc[mask, "Appearances"].values
        if len(index_list) == 0:
            return pd.DataFrame()
        else:
            return self.df.loc[index_list[0]]


    def filter_by_frequency(self):
        """
        Filter out words with frequency outside a specified range
        :return: a filtered dataframe
        """
        f1 = 0
        f2 = float(input("High frequency words such as gmbh cause issues "
                         "Enter the cutoff frequency : For example 30."))

        self.words_df = self.words_df[(self.words_df['Frequency'] >= f1) & (self.words_df['Frequency'] <= f2)].copy()
        return self.words_df


    def drop_words(self,):
        """ Did not use """
        drop_words = pd.read_csv(words_to_drop)['Word'].tolist()
        self.words_df = self.words_df[~self.words_df['Word'].isin(drop_words)]


    def describe_df(self, n1=0, n2=20):
        print(f"The dataframe :\n {self.words_df}")
        print(f"\nSize of the dataframe : {self.words_df.shape}")
        print(f"\nExamples from rows n1 to n2:\n {self.words_df[n1:n2]}")
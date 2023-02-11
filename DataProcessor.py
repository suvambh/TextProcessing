import pprint
import pandas as pd
import numpy as np
from collections import defaultdict
from gensim.models import Word2Vec
from gensim.models import FastText
from gensim.test.utils import datapath
from sklearn.cluster import KMeans
import logging
import matplotlib.pyplot as plt

# Configure logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class DataProcessor:



    def __init__(self, data_frame):
        self.data_frame = data_frame

    def sort_words_in_language(self, language='en', col='Raw name'):
        name_by_language = self.data_frame[self.data_frame['Language'] == language][col]
        text_corpus = pd.DataFrame(data=name_by_language)
        client_names = [name.split() for name in text_corpus[col]]
        word_frequencies = defaultdict(int)
        for name in client_names:
            for word in name:
                word_frequencies[word] += 1
        sorted_words = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)
        return sorted_words

    def plot_word_frequencies(self, top_words, sorted_words):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
        ax1.bar([word[0] for word in top_words], [word[1] for word in top_words])
        ax1.set_xlabel("Word")
        ax1.set_ylabel("Frequency")
        ax1.set_title("Frequency of Top 30 Words")
        ax1.tick_params(axis='x', labelrotation=90)
        ax2.hist([frequency for word, frequency in sorted_words], bins=100, edgecolor='black')
        ax2.set_xlabel("Frequency")
        ax2.set_ylabel("Number of Words")
        ax2.set_title("Frequency Distribution")
        ax2.set_xlim(0, 100)
        ax2.set_ylim(0, 50)
        plt.tight_layout()
        plt.show()

    def remove_frequent_words(self, sorted_words, num_words_to_remove):
        dictionary_sorted = dict(sorted_words)
        most_frequent_words = list(dictionary_sorted.keys())[:num_words_to_remove]
        for word in most_frequent_words:
            self.data_frame['Raw name'] = self.data_frame['Raw name'].str.replace(word, '')
        duplicates = self.data_frame[self.data_frame.duplicated(keep=False)]
        print("Duplicates:")
        print(duplicates)
        mask = ~data_frame['Raw name'].isin(duplicates)
        return (data_frame[mask])

def main():
    # Load the data into a pandas dataframe
    data_frame = pd.read_csv("normalised.csv")

    # Initialize the DataProcessor class with the data_frame
    data_processor = DataProcessor(data_frame)

    # Sort the words in the language of interest
    sorted_words = data_processor.sort_words_in_language()

    # Plot the word frequencies
    data_processor.plot_word_frequencies(sorted_words[:30], sorted_words)

    # Remove the top N frequent words
    N = 5
    data_processor.remove_frequent_words(sorted_words, N)

if __name__ == '__main__':
    main()

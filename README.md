# Text_processing_project
 # Introduction
This is a code repository for a data processing pipeline that analyzes and modifies a CSV file of names. The code leverages the power of pandas library to process the data and the gensim library to train word embeddings. The output of the code is a cleaned data frame with reduced number of frequently occurring words and a histogram showing the frequency distribution of words.

## Requirements
The code requires the following libraries:
- pandas
- numpy
- gensim
- matplotlib
- sklearn

## Data Processing Pipeline
The code performs the following steps to process the data:
1. Loads the data into a pandas dataframe
2. Initializes the DataProcessor class with the data_frame
3. Sorts the words in the language of interest (English by default)
4. Plots the word frequencies
5. Removes the top N frequent words

## Classes and Methods
### DataProcessor
The DataProcessor class takes the data frame as an input and performs the following operations:
- `sort_words_in_language`: This method takes the language and the column name as inputs and returns a list of tuples containing words and their frequency.
- `plot_word_frequencies`: This method takes two inputs - the list of top words and the sorted words. It plots a bar graph of the frequency of the top words and a histogram of the frequency distribution of all words.
- `remove_frequent_words`: This method removes the top N frequent words from the data frame.

## Conclusion
This code pipeline provides a simple and straightforward solution to process a data frame containing names and performs several common data processing operations like sorting, plotting and removing frequent words. This can be a good starting point for further data processing and analysis.

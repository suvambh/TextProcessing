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



### DataToMap
The DataToMap is a Python class that allows you to convert data stored in a Pandas DataFrame into a word frequency mapping. This class can be used to analyze text data and extract meaningful insights from it.

#### Class Constructor
The constructor for the class takes two arguments:

1. df : a pandas DataFrame object
2. column_name : a string representing the column name in the DataFrame to be analyzed
#### Methods
The class includes several methods:

1. map_data : splits the data stored in the specified column of the DataFrame and stores the words and their indices in separate lists.
2. create_word_df : creates a DataFrame to store the word data.
3. group_word_df : groups the words based on the frequency of their appearance.
4. count_frequency : adds a column to the DataFrame to store the frequency of each word.
5. search : returns the row from the original DataFrame where the specified word appears.
6. add_is_number_column : adds a column to the DataFrame to indicate whether each word is a number or not.
7. describe_df : prints some information about the DataFrame.
8. Main Function
The main function creates an instance of the class, applies the methods on the data and prints some information about the resulting word frequency mapping DataFrame.


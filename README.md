# Text Processing 
# Introduction
This is a code repository for a data processing project that analyzes and modifies file of names of companies.
# Intuition 
This algorithm aims to predict the most probable company name based on word frequency and a fuzzy matching score. The input to the algorithm is a company name, which is split into individual words. The algorithm then searches a pre-existing database for each word, looking for a match in the company names. For each match, the algorithm computes a score that combines the frequency of the word in the company name and a fuzzy matching score that quantifies the similarity between the input name and the company name. The scores are weighted by parameters a, b, p, and q to control the importance of each factor.

The algorithm then normalizes the score values and returns the company name with the highest score as the predicted name. In cases where the input name does not match any name in the database, the algorithm returns the input name itself.

Intuitively, the algorithm is trying to identify the most likely company name by leveraging information about the frequency of words in company names and how similar the input name is to existing names. By combining these factors, the algorithm is able to make an informed guess about the most probable company name.

## Requirements:
This module requires Python version 3.x and the following packages:

Pandas <br>
NumPy <br>
ConfigParser <br>
Fuzzywuzzy

## Data Cleaning 

The data_cleaning.py module uses TextCleaner class for cleaning and preprocessing data stored in a Pandas DataFrame. The methods in this class include:

<b>remove_duplicates:</b> removes duplicate rows from the input DataFrame.<br>
<b>drop_na:</b> removes rows with missing values from the input DataFrame.<br>
<b>fill_na:</b> fills missing values in the input DataFrame with the specified value or method.<br>
<b>replace_values:</b> replaces specified values in the input DataFrame with a new value.<br>

The output file is named  <b>normalised.csv</b>

## Data Processing 

### Classes 

#### DataToMap

Takes a Pandas DataFrame as input and provides methods to extract and creates a map from the data.<br>

Methods: <br>

<b>map_data:</b> extracts all the words from the input data and their corresponding index where they appear.<br>
<b>create_words_df:</b> creates a dataframe with unique words and their frequency of occurrence.<br>
<b>group_words_df:</b> groups words in the dataframe based on their value and creates a list of indices where the word appears.<br>
<b>count_frequency:</b> counts the frequency of each word in the input data.<br>
<b>search:</b> searches for a word in the dataframe and returns the corresponding rows from the input data.<br>
<b>filter_by_frequency:</b> filters out words with frequency outside a specified range.<br>
<b>drop_words:</b> drops words from the dataframe as specified in the list of words to drop (not used).<br>
<b>describe_df:</b> prints a description of the dataframe, including its size and examples of rows from n1 to n2.<br>

### GuessFromName 

#### Attributes:

<b>name :</b> The name to guess from.<br>
<b>df :</b> The data frame containing company names.<br>
<b>words_df :</b> The data frame containing word frequencies.<br>
<b>p (int):</b> fuzz ratio with coefficient <b>a (int)</b> raised to the power of p.</br>
<b>q (int):</b> fuzz ratio with coefficient <b>a (int)</b> raised to the power of p.</br>

#### Methods:

<b>fuzzy_frequency_guess :</b>

This function calculates the most probable company name based on word frequency and fuzziness score. 
It does this by : 
1. Splits the name into words and creates a dictionary to store the score of each company name.
2. Loops through each word in the list and calculates the score of each company by weighting the frequency of words in the company name and the fuzzy matching score using the parameters a, b, p, and q.
3. Normalizes the score values and returns the company name with the highest score and the score.<br>

<br>
<b>predict_companies_from_df :</b>

Returns a list of probable company names and scores for each name in the given DataFrame (df). It does this by. 
1. Iterates through each row of the DataFrame and creates a GuessFromName object to calculate the most probable company name and score using the fuzzy_frequency_guess function.
2. Appends the name and score to separate lists.
3. Adds a new column to the original DataFrame with the mapped company names and scores.

<b>guess_df :</b> <br>
Calls predict_companies_from_df to map company names to a DataFrame.
Returns the mapped DataFrame.
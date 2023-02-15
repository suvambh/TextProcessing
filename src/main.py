import pandas as pd
from map_generator import DataToMap
from guess_algorithms import GuessFromName
import configparser


def main():
    # Load config file
    config_path = '../settings/config.ini'
    config = configparser.ConfigParser()
    config.read(config_path)

    # Load data from the normalised data file specified in config file
    normalised_data_path = config['file_paths']['normalised_data']
    data = pd.read_csv(normalised_data_path)
    print(f"Data Loaded: \n{data.head(3)}")

    # Generate map from data and create words dataframe
    map_object = DataToMap(data)
    word, appears_at = map_object.map_data()
    words_df = map_object.create_words_df(word, appears_at)

    # Group and filter the words dataframe
    words_df = map_object.group_words_df()
    words_df = map_object.count_frequency()
    words_df = map_object.filter_by_frequency()

    # Guess input name and generate guess dataframe
    input_name = "alteryx"
    p, q, a, b = 0, -1, 1, 1 # Parameters to tune the model. Check fuzzyfrequencyguess score to see how this is used.
    obj = GuessFromName(input_name, data, words_df, p, q, a, b)
    print(obj.fuzzy_frequency_guess())
    guessed_df = obj.guess_df()

    # Write the guess dataframe to the file specified in config file
    guess_map_path = config['file_paths']['guess_map']
    guessed_df.to_csv(guess_map_path)
    print(f"Generated {guess_map_path} with success for parameters p={p}, q={q}, a={a}, b={b}")

    # Print the guess dataframe
    print(guessed_df)


if __name__ == '__main__':
    # Enter path to config.ini
    main()




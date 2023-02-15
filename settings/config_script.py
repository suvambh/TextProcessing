import configparser

# create a new configuration file
config = configparser.ConfigParser()

config['file_paths'] = {}
config['file_paths']['raw_data'] = '../data/Case_study_names_mapping.xlsx'
config['file_paths']['normalised_data'] = '../csv_data_cleaned/normalised.csv'
config['file_paths']['guess_map'] = '../csv_data_cleaned/guess_map.csv'
config['file_paths']['words_df'] = '../csv_data_cleaned/words_df.csv'

config['file_paths']['config_file'] = '../settings/config.ini'
config['file_paths']['words_to_drop'] = '../csv_data_cleaned/words_to_drop.csv'

with open(config['file_paths']['config_file'], 'w') as configfile:
    config.write(configfile)


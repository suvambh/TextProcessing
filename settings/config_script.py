import configparser

# create a new configuration file
config = configparser.ConfigParser()

# add a section to the file
config['file_paths'] = {}
# add some values to the section
config['file_paths']['raw_data'] = '../data/Case_study_names_mapping.xlsx'
config['file_paths']['normalised_data'] = '../csv_data_cleaned/normalised.csv'
config['file_paths']['guess_max_freq'] = '../csv_data_cleaned/guess_max_freq.csv'
config['file_paths']['config_file'] = '../settings/config.ini'

# save the configuration file
with open(config['file_paths']['config_file'], 'w') as configfile:
    config.write(configfile)


config2 = configparser.ConfigParser()

config2.read('config.ini')

raw_data = config2['file_paths']['raw_data']
normalised_data = config2['file_paths']['normalised_data']
guess_max_freq = config2['file_paths']['guess_max_freq']

print(raw_data, normalised_data, guess_max_freq)

# Use the input and output file paths in your code

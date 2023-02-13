import pandas as pd
from map_making import DataToMap
import cluster_ai

def main(data, column_name):
    map_object = DataToMap(data, column_name)
    words, appears_at = map_object.map_data()
    word_df = map_object.create_word_df(words, appears_at)
    word_df = map_object.group_word_df()
    word_df = map_object.count_frequency()
    word_df = map_object.add_is_number_column()
    map_object.describe_df()
    print(map_object.search("4d"))

if __name__ == '__main__':
    data = pd.read_csv("../csv_data_cleaned/normalised2.csv")
    main(data,'Raw name')


import pandas as pd
from map_making import DataToMap
from cluster_ai import GuessByFrequency

def main(data, column_name):
    map_object = DataToMap(data, column_name)
    words, appears_at = map_object.map_data()
    word_df = map_object.create_word_df(words, appears_at)
    word_df = map_object.group_word_df()
    word_df = map_object.count_frequency()
    word_df = map_object.add_is_number_column()

    input_name = "a paris production"

    obj = GuessByFrequency(input_name, data, word_df, threshold=0.)
    print(obj.probabilistically_guess_company())
    print(obj.guess_get_df())

    #map_object.describe_df()
    #print(map_object.search("4d"))

if __name__ == '__main__':
    data = pd.read_csv("../csv_data_cleaned/normalised2.csv")
    print(data.head(3))
    main(data,'Raw name')
    data.to_csv("/Users/suvam/Documents/Text_processing_project/csv_data_cleaned/guess_max_freq.csv")

    #data[data['Raw name'].str.contains("Amicale")]



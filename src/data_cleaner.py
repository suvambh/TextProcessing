
import pandas as pd
import re
from langdetect import detect

class TextProcessing:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_excel(file_path)

    def preprocess(self):
        self.df.drop_duplicates(subset='Raw name', keep='first', inplace=True)
        self.df["Raw name"] = self.df["Raw name"].apply(lambda x: re.sub(r'[^\w\s]', '', x))
        self.df["Raw name"] = self.df["Raw name"].str.lower().str.strip()

    def detect_language(self):
        def detect_language(name):
            return detect(name)
        self.df['Language'] = self.df['Raw name'].apply(detect_language)

    def save(self):
        self.df.to_csv('normalised2.csv', index=False)
        self.df_imported = pd.read_csv('../csv_data_cleaned/normalised2.csv')


if __name__ == '__main__':
    file_path = "/data/Case_study_names_mapping.xlsx"
    # Initialize the TextProcessing class with the file path
    text_processor = TextProcessing(file_path)
    text_processor.preprocess()
    text_processor.detect_language()
    # Save the processed data
    text_processor.save()

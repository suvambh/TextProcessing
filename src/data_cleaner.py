
import pandas as pd
import re

class TextProcessing:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_excel(file_path)
        self.preprocess()
    def preprocess(self):
        self.df.drop_duplicates(subset='Raw name', keep=False, inplace=True)
        self.df["Raw name"] = self.df["Raw name"].apply(lambda x: re.sub(r'[^\w\s]', '', x))
        self.df["Raw name"] = self.df["Raw name"].str.lower().str.strip()

    def save(self):
        self.df.to_csv('../csv_data_cleaned/normalised.csv', index=False)

if __name__ == '__main__':
    file_path = "../data/Case_study_names_mapping.xlsx"
    # Initialize the TextProcessing class with the file path
    text_processor = TextProcessing(file_path)
    text_processor.save()

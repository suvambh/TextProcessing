import configparser
import pandas as pd
import re


class TextCleaner:
    def __init__(self, ):
        config = configparser.ConfigParser()
        config.read('../settings/config.ini')
        self.input_path = config['file_paths']['raw_data']
        self.save_path = config['file_paths']['normalised_data']
        self.df = pd.read_excel(self.input_path)
        self.normalize_text()

    def normalize_text(self):
        "Remove spaces"
        self.df['Raw name'] = self.df['Raw name'].apply(lambda x: re.sub(r'\s+', ' ', x))
        self.df.drop_duplicates(subset='Raw name', keep=False, inplace=True)
        self.df["Raw name"] = self.df["Raw name"].apply(lambda x: re.sub(r'[^\w\s]', '', x))
        self.df["Raw name"] = self.df["Raw name"].str.lower().str.strip()
        # Merge single characters separated by a space with a period
        pattern = r'\b([a-zA-Z])\s+([a-zA-Z])\b'
        self.df['Raw name'] = self.df['Raw name'].apply(lambda x: re.sub(pattern, r'\1.\2', x))

    def save(self):
        self.df.to_csv(self.save_path, index=False)


if __name__ == '__main__':
    # Initialize the TextProcessing class obj
    text_processor = TextCleaner()
    text_processor.save()

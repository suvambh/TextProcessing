import streamlit as st
from src import main
import pandas as pd
import matplotlib.pyplot as plt



class StreamlitInterface:
    def __init__(self, data, sample_size=4895):
        self.data_processor = main.dataprocess(data, sample_size)
        self.sorted_bag_of_words = self.data_processor.sorted_bag_of_words
        self.flagged_rows = []
        self.temp = []

    def get_sample_size(self):
        sample_size = st.text_input("Enter N (integer) :")
        if sample_size.isdigit():
            return int(n)
        else:
            st.write("Error: Please enter a valid integer")
            return 0

    def get_N(self):
        n = st.text_input("Enter N (integer) :")
        if n.isdigit():
            return int(n)
        else:
            st.write("Error: Please enter a valid integer")
            return 0


    def plot_top_n_words(self):
        # Get the top N words and their frequencies from sorted_bag_of_words
        n = 10

        top_n_words = dict(list(self.sorted_bag_of_words.items())[:n])
        words = top_n_words.keys()
        frequencies = top_n_words.values()

        # Plot the frequency of words vs the words
        fig, ax = plt.subplots()
        ax.bar(words, frequencies)
        ax.set_xlabel("Words")
        ax.set_ylabel("Frequency")
        st.pyplot(fig)


    def filter_by_word(self, word):
        return self.data_processor.data_frame['Raw name'][self.data_processor.data_frame['Raw name'].apply(lambda x: word in x)]

    def get_word(self):
        word = st.text_input("Enter a word:")
        return word

    def check_box(self, rows):
        selected_rows = []

        if st.button("Submit"):
            for row in rows:
                if row in st.button_map:
                    selected_rows.append(row)
            self.flagged_rows.extend(selected_rows)
            st.write("Selected rows have been added to self.flagged_rows.")
        return selected_rows

    def generate(self):
        word = self.get_word()
        filtered_data = self.filter_by_word(word)
        st.write("Data containing the word:", word)
        rows = filtered_data[0:30].T
        with st.form(key='button_map'):
            for row in rows:
                st.checkbox(str(row))
            st.form_submit_button()
        selected_rows = self.check_box(rows)

        st.write("Selected rows:")
        st.write(rows.loc[selected_rows].T)


if __name__ == "__main__":
    data = pd.read_csv('../csv_data_cleaned/normalised2.csv')
    print("Hello", len(data))
    data = data.drop(columns=['Mapped name', 'Language',])
    data.reset_index()
    print(data.index, data.head(5), data.tail(5))


    streamlit_interface = StreamlitInterface(data)
    streamlit_interface.plot_top_n_words()
    rows = streamlit_interface.generate()



    #streamlit_interface.check_box()

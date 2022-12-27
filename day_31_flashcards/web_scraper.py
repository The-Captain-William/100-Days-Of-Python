import pandas as pd
import lxml


# get html page
chinese_0_to_1k = pd.read_html("https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_lists/1-1000")

# html produces list of dataframes, list index zero is our dataframe
chinese_0_to_1k_dataframe = chinese_0_to_1k[0]

# delete traditional on axis 1 (axis 1 == column, axis 0 == row)
to_csv = chinese_0_to_1k_dataframe.drop(["Traditional"], axis=1)

# drop empty rows, any kwarg ❓ not sure what any does
to_csv.dropna(axis=0, how='any')

# compiled to csv
to_csv.to_csv("First 1000 Characters 1.0.csv", index=False)

# opened again and selected Pinyin column
data = pd.read_csv("First 1000 Characters 1.0.csv", index_col="Pinyin")
# drop all columns with the word (file in them) ❓ not sure what in place kwarg is for
data.drop("(file)", inplace=True)
# compile to csv
data.to_csv("first_1000_chars.csv")


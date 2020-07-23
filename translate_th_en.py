# A script that iterates through a .xlsx file and translates any cells with Thai text to English.

# For a person on the internet.

# You will need to run: 'pip3 install googletrans' (downloads the translation package)
#                       'pip3 install openpyxl' (tells pandas how to write to .xlsx properly)


from textblob import TextBlob
import pandas as pd
from random import randint
df = pd.read_excel("file.xlsx") # Replace file.xlsx with the file name that you're reading from
for i, row in df.iterrows():
    for column in df.columns:
        cell_text = str(row[column])
        try:
            if TextBlob(cell_text).detect_language() == 'th':
                translation = translator.translate(cell_text, src='th',dest='en')
                row[column] = translation.text
        except:
            pass
df.to_excel('newfile{}.xlsx'.format(randint(0,999999)), index=False)

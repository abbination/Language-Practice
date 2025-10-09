#First step in the pipeline. 
#TO DO: set up load into database and ways to interact with the data

#Import needed libraries
import pandas as pd
from pathlib import Path
import os
import openpyxl

#Get the current script's folder
root_dir = os.getcwd()

#Form the complete file path
file_path = os.path.join(root_dir, 'VocabList.xlsx')

#Extract the first sheet of the file
df_verbs = pd.read_excel(file_path, sheet_name="Verbs")

#Extract the second sheet of the file
df_nouns = pd.read_excel(file_path, sheet_name="Nouns")

#Extract the third sheet of the file
df_adj = pd.read_excel(file_path, sheet_name="Adjectives")

#Extract the fourth sheet of the file
df_adv = pd.read_excel(file_path, sheet_name="Adverbs")

#Extract the fifth sheet of the file
df_prep = pd.read_excel(file_path, sheet_name="Prepositions")

#Extract the sixth sheet of the file
df_phrase = pd.read_excel(file_path, sheet_name="Phrases")
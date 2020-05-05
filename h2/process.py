import pandas as pd

path = 'newSheet.csv'

file = pd.read_csv('sheet.csv')

file["ep"].fillna("Nan", inplace = True) 
file["people"].fillna("Sam Wlat", inplace = True) 
#export 
file.to_csv (path, index = False, header=True)
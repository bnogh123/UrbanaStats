import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt

# Grab and process the raw data.
data_path = ("https://data.illinois.gov/dataset/1d18ecc0-3c7e-4507-b8cc-7a5e30359d44/"
             "resource/ca1dceb3-01f8-4a56-935b-7e3035ff60a4/download/"
             "police-arrests-upload_20191226.csv")
arr_raw = pd.read_csv(data_path, delimiter=',')

# Cut into subset
arr_raw2 = arr_raw[['arrestee_race', 'year_of_arrest']]

# Define unique values
years = arr_raw2.year_of_arrest.unique()
races = arr_raw2.arrestee_race.unique()

temp = np.zeros((years.size,
                 races.size))

# iterate through years
for i in range(years.size):
    yearly = (arr_raw2['year_of_arrest'] == years[i]).size
    for j in range(races.size):
        temp[i, j] = arr_raw2[(arr_raw2['arrestee_race'] == races[j]) | (
                    arr_raw2['year_of_arrest'] == years[i])].size / yearly * 100.0

# move values to dataframe
r_arrests = pd.DataFrame({'year': years})
r_arrests = pd.concat([r_arrests, pd.DataFrame(temp)], axis=1)

col = np.insert(races, 0, 'year')
r_arrests.columns = col

print(r_arrests)

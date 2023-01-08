import os, json
import pandas as pd
import numpy as np
import glob

df_traffy = pd.DataFrame()

path_to_json = 'json-data/*.json' 
#path_to_json = 'dec12.json'
#Path to the JSON files
traffy_files = glob.glob(path_to_json)

for count,ele in enumerate(traffy_files,len(traffy_files)):
    df_traffy = pd.concat([df_traffy, pd.read_json(ele)])

df_traffy.to_csv("df_traffyfull.csv",index=False)


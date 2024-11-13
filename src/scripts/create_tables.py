import pandas as pd
import sys
import numpy as np

def create_master_rating_table():
  sys.path.append('../../pickles')
  imdb = pd.read_pickle('pickles/imdb_data.pkl')
  metacritic = pd.read_pickle('pickles/metacritic_df.pkl')
  rotten_tomatoes = pd.read_pickle('pickles/rotten_tomatoes.pkl')
  print(imdb.head())

create_master_rating_table()
import pandas as pd
import sys
import numpy as np

def create_master_rating_table():
  sys.path.append('../../pickles')
  cmu_movies = pd.read_pickle('pickles/cmu_movies_df.pkl')
  imdb = pd.read_pickle('pickles/imdb_data.pkl')
  metacritic = pd.read_pickle('pickles/metacritic_df.pkl')
  rotten_tomatoes = pd.read_pickle('pickles/rotten_tomatoes.pkl')
  character_metadata = pd.read_pickle('pickles/character_metadata.pkl')
  
  dfs = {"cmu": cmu_movies, 
                 "imdb": imdb, 
                 "metacritic": metacritic, 
                 "rotten_tomatoes": rotten_tomatoes,
                 "characters": character_metadata
                 }

  for dataset in dfs.keys():
    print(f'Dataset {dataset} INFO:')
    df = dfs[dataset]
    df.info()
    # print(f'Info: {df.info()}')
    # print(f'Columns: {df.columns}')
    print()

create_master_rating_table()
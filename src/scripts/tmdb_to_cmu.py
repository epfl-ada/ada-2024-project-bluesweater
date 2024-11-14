import pandas as pd
import sys
import unidecode

def tmdb1m_to_pickle():
  """
  Use initially, to extract the data into a pickle data frame
  """
  sys.path.append('../../data')
  sys.path.append('../../pickles')

  tmdb_df = pd.read_csv('data/tmdb/TMDB_all_movies.csv')
  tmdb_df.to_pickle('pickles/tmdb1m')


def join_on_movie_name(cmu_df, extra_df): # does not work as intended - do not use this method
  # cmu_df['clean_movie_name'] = cmu_df['Movie Name'].apply(
  #   lambda x: unidecode.unidecode(str(x).strip().lower().replace(' ', ''))
  # )
  # extra_df['clean_movie_name'] = extra_df['title'].apply(
  #   lambda x: unidecode.unidecode(str(x).strip().lower().replace(' ', ''))
  # )

  cmu_df['clean_movie_name'] = cmu_df['Movie Name']
  extra_df['clean_movie_name'] = extra_df['title']

  merged_df = pd.merge(cmu_df, extra_df, on='clean_movie_name', how='left')
  return merged_df

def tmdb_to_cmu():
  sys.path.append('../../data')
  sys.path.append('../../pickles')

  cmu_df = pd.read_pickle('pickles/cmu_movies_df.pkl')
  tmdb_df = pd.read_pickle('pickles/tmdb1m')
  # tmdb_df = pd.read_csv('data/tmdb/TMDB_all_movies.csv')

  print(tmdb_df.columns)

  cmu_df.info()
  tmdb_df.info()

  return join_on_movie_name(cmu_df, tmdb_df) # TODO replace with join_on_imdb

# tmdb1m_to_pickle()
merged_df = tmdb_to_cmu()
print(merged_df.columns)
merged_df.info()

print(merged_df.head(10)[['Movie Name', 'Release Date', 'release_date']])

# print(len(merged_df['Movie Name'].unique()))
# print(len(merged_df['clean_movie_name'].unique()))

# Find duplicates in the merged DataFrame based on 'clean_movie_name'
duplicates_in_merged_df = merged_df[merged_df.duplicated(subset='clean_movie_name', keep=False)]

# Display the duplicates
print(duplicates_in_merged_df)

# Create a new column that flags duplicates
merged_df['is_duplicate'] = merged_df.duplicated(subset='clean_movie_name', keep=False)

# Display rows that are duplicates
# for i, entry in merged_df[merged_df['is_duplicate']].iterrows():
#   print(i, entry)

# print(merged_df[merged_df['is_duplicate']])
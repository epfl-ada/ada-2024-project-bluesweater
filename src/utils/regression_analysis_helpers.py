import pandas as pd

def one_hot_encode(df, columns=['production_companies', 'director', 'writers', 'producers']):
  for col in columns:
    # Split each value on ', ' and create a column for each value (dummy encoding)
    dummies = df[col].str.get_dummies(sep=', ')
    # Rename the columns to include the original column name as a prefix
    dummies.columns = [f"{col}_{c}" for c in dummies.columns]
    # Concatenate the dummy columns to the original dataframe
    df = pd.concat([df, dummies], axis=1)
    # Drop the original column
    df.drop(col, axis=1, inplace=True)

def frequency_encode(df, columns=['production_companies', 'director', 'writers', 'producers']):
  df[columns] = df[columns].astype(str)
  
  for col in columns:
    # Explode the column to create one row per item in the list (if values are lists or comma-separated)
    if df[col].apply(lambda x: isinstance(x, str)).all():
      df[col] = df[col].apply(lambda x: x.split(', ') if isinstance(x, str) else x)
    exploded_df = df.explode(col)

    # Calculate frequency of each unique value in the column
    col_freq = exploded_df[col].value_counts()

    # Map the frequency encoding back to the original DataFrame, adding / averaging for multiple contributors
    df[f'{col}_frequency_encoded'] = df[col].apply(
      lambda x: sum(col_freq[val] for val in x if val in col_freq) if isinstance(x, list) else None # encode with sum
    ) 
    # df[f'{col}_frequency_encoded'] = df[col].apply(
    #   lambda x: sum(col_freq[val] for val in x if val in col_freq) / len(x) if isinstance(x, list) else None # encode with avg
    # )

  return df

def target_encode(df, columns=['production_companies', 'director', 'writers', 'producers'], target_col='Box Office Revenue', encode_func=pd.Series.mean):
  df[columns] = df[columns].astype(str)

  for col in columns:
    # Explode the column to create one row per item in the list (if values are lists or comma-separated)
    if df[col].apply(lambda x: isinstance(x, str)).all():
      df[col] = df[col].apply(lambda x: x.split(', ') if isinstance(x, str) else x)
    exploded_df = df.explode(col)

    # Calculate the target encoding (mean, median, etc.) for each unique value in the column
    col_target_mean = exploded_df.groupby(col)[target_col].apply(encode_func)

    # Map the encoding back to the original DataFrame, averaging for multiple contributors
    df[f'{col}_encoded'] = df[col].apply(
      lambda x: sum(col_target_mean[val] for val in x if val in col_target_mean) / len(x) if isinstance(x, list) else None
    )

  return df

def format_release_date(df):
  # Ensure the 'Release Date' column is not null before processing
  date_not_nan = df[df['Release Date'].notnull()]['Release Date']
  
  # Split the date strings by '-' into lists
  date_not_nan = date_not_nan.str.split('-')

  # Iterate over the rows
  for i, date in date_not_nan.items():
    # Assign year, month, and day based on the length of the split date
    if len(date) == 1:
      df.at[i, 'Release Year'] = int(date[0])
    elif len(date) == 2:
      df.at[i, 'Release Year'] = int(date[0])
      df.at[i, 'Release Month'] = int(date[1])
    elif len(date) == 3:
      df.at[i, 'Release Year'] = int(date[0])
      df.at[i, 'Release Month'] = int(date[1])
      df.at[i, 'Release Day'] = int(date[2])

  # Convert the columns to integer, preserving NaNs
  df['Release Year'] = df['Release Year'].astype('Int64')
  df['Release Month'] = df['Release Month'].astype('Int64')
  df['Release Day'] = df['Release Day'].astype('Int64')

  return df

def one_hot_encode_month(df):
  # Create one-hot encoded columns for the 'Release Month' column
  month_dummies = pd.get_dummies(df['Release Month'], prefix='Month', dummy_na=False)

  # Concatenate the one-hot encoded columns with the original dataframe
  df = pd.concat([df, month_dummies], axis=1)

  return df
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

### DATA cleaning ###
def plot_missing_data(df):
  x = df.columns
  y = np.sum(df.isnull())
  y = y[y > 0]
  y = y.sort_values(ascending=False)
  sns.barplot(y)
  plt.title(f"Number of missing values (out of {len(df)})")
  plt.xticks(rotation=90, fontsize=10)
  for i, v in enumerate(y):
    plt.text(i, v + 2, str(v), ha='center', fontsize=10)

  plt.show()

### GENERAL ANALYSIS ###
def plot_gender_distribution(df):
  # 1. 2. Total count & Gender distribution for each trope
  fig, (a0, a1) = plt.subplots(2,1, figsize=(14, 12), height_ratios=[1,2])
  gender_counts = df['actor_gender'].value_counts()
  gender_counts.plot(kind='pie', title='Gender distribution in the dataset', ax=a0, autopct='%1.1f%%')

  gender_trope_counts = df.groupby(['trope', 'actor_gender']).size().unstack(fill_value=0)
  gender_trope_counts = gender_trope_counts.loc[gender_trope_counts.sum(axis=1).sort_values(ascending=False).index]
  gender_trope_counts.plot(kind='bar', stacked=True, title='Gender Distribution for Each Trope', ax=a1, grid=True)

def plot_age_distribution(df):
  plt.figure(figsize=(14, 6))
  sorted_df = df.sort_values(by='actor_age_at_release')
  sns.boxplot(x='trope', y='actor_age_at_release', data=sorted_df)
  plt.xticks(rotation=90)
  plt.title('Age Distribution for Each Trope')

def plot_runtime_distribution(df):
  plt.figure(figsize=(14, 6))
  sns.boxplot(x='trope', y='Runtime', data=df)
  plt.xticks(rotation=90)
  plt.title('Trope vs. Runtime Relationship')

def plot_full_general_analysis(df):
  plot_gender_distribution(df)
  plot_age_distribution(df)
  plot_runtime_distribution(df)

### BOX OFFICE ANALYSIS ###
def plot_success_metric_missing(df: pd.DataFrame, success_metric='box_office'):
  """
  Plots the proportion of tropes missing
  """

  # Count the total number of movies per trope
  total_movies_per_trope = df['trope'].value_counts()

  # Count the number of movies with missing box office per trope
  missing_success_metric = df[df[success_metric].isnull()]['trope'].value_counts()

  # Create a DataFrame to hold both counts
  trope_counts = pd.DataFrame({
      'Box Office Not Missing': total_movies_per_trope,
      'Missing Box Office': missing_success_metric
  })

  # Fill NaNs in the 'Missing Box Office' column with 0 for tropes with no missing data
  trope_counts['Missing Box Office'] = trope_counts['Missing Box Office'].fillna(0)
  trope_counts['Box Office Not Missing'] -= trope_counts['Missing Box Office']  # subtract the movies missing

  # Calculate the proportion of movies missing box office data
  trope_counts['Proportion Missing'] = trope_counts['Missing Box Office'] / (trope_counts['Box Office Not Missing'] + trope_counts['Missing Box Office'])

  # Sort by the proportion of missing data
  trope_counts = trope_counts.sort_values(by='Proportion Missing', ascending=False)

  # Plot a stacked bar chart
  trope_counts[['Box Office Not Missing', 'Missing Box Office']].plot(kind='bar', stacked=True, figsize=(14, 6))
  for i, missing in enumerate(trope_counts['Proportion Missing']):
    plt.text(i, trope_counts['Box Office Not Missing'][i] + trope_counts['Missing Box Office'][i] + 0.5, int(missing*100), fontsize='xx-small', ha='center')
  plt.title(f'Total Number of Movies and Missing {success_metric} Data per Trope (Sorted by Percentage Missing)')
  plt.xlabel('Trope')
  plt.ylabel('Number of Movies')
  plt.show()
  return

def plot_success_metric_per_trope(df: pd.DataFrame, success_metric='box_office'):
  """
  Plot the gross per trope
  """
  # Count the total number of movies per trope
  total_movies_per_trope = df['trope'].value_counts()

  # Count the number of movies with missing box office per trope
  missing_success_metric = df[df[success_metric].isnull()]['trope'].value_counts()

  # Create a DataFrame to hold both counts
  trope_counts = pd.DataFrame({
      'Box Office Not Missing': total_movies_per_trope,
      'Missing Box Office': missing_success_metric
  })

  # Fill NaNs in the 'Missing Box Office' column with 0 for tropes with no missing data
  trope_counts['Missing Box Office'] = trope_counts['Missing Box Office'].fillna(0)
  trope_counts['Box Office Not Missing'] -= trope_counts['Missing Box Office']  # subtract the movies missing

  gross_per_trope = df.groupby('trope')[success_metric].sum() / trope_counts['Box Office Not Missing']
  gross_per_trope.sort_values().plot(kind='bar', figsize=(14, 6), title=f'Total {success_metric} per Trope (Adjusted by Character Count)')
  plt.show()

def plot_trope_genre_heatmap(df, threshold = 600000000, success_metric='box_office'):
  # Ensure 'Genre Name' column is treated as a list and explode it
  df_exploded = df.explode('Genre Name')

  # Create the pivot table using the exploded DataFrame
  trope_genre_success_metric = df_exploded.pivot_table(
      values=success_metric,
      index='trope',
      columns='Genre Name',
      aggfunc='mean'
  )

  # Filter the pivot table to only include values above the threshold
  filtered_trope_genre_success_metric = trope_genre_success_metric.where(trope_genre_success_metric > threshold)

  # Drop rows and columns that are all NaNs (i.e., those not meeting the threshold)
  filtered_trope_genre_success_metric = filtered_trope_genre_success_metric.dropna(how='all', axis=0).dropna(how='all', axis=1)

  # Plot the heatmap with filtered data
  plt.figure(figsize=(14, 10))
  sns.heatmap(filtered_trope_genre_success_metric, annot=False, cmap='viridis')
  plt.title(f'Trope-Genre Relationship (Average Box Office > {threshold})')
  plt.show()

def plot_trope_gender_success_metric(df, success_metric='box_office'):
  plt.figure(figsize=(14, 20))
  trope_gender_success_metric = df.pivot_table(values=success_metric, index='trope', columns='actor_gender', aggfunc='mean')
  sns.heatmap(trope_gender_success_metric, annot=True, cmap='magma')
  plt.show()

def plot_age_success_metric(df, success_metric='box_office'):
  plt.figure(figsize=(14, 6))
  sns.scatterplot(x='actor_age_at_release', y=success_metric, hue='trope', data=df)
  plt.show()

def show_most_successful_tropes(df, items=5, success_metric='box_office'):
  trope_success_metric_mean = df.groupby('trope')[success_metric].mean().sort_values(ascending=False)
  trope_success_metric_mean = trope_success_metric_mean.astype(int)  # Convert to integer
  print(trope_success_metric_mean.head(items))  # Show top 10 tropes

def plot_full_box_office_analysis(df, success_metric='box_office'):
  plot_success_metric_missing(df, success_metric)
  plot_success_metric_per_trope(df, success_metric)
  plot_trope_genre_heatmap(df, success_metric)
  plot_trope_gender_success_metric(df, success_metric)
  plot_age_success_metric(df, success_metric)
  show_most_successful_tropes(df, success_metric)


import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON
import sys
import requests

sys.path.append('../../data')
sys.path.append('../../pickles')

# Load your CSV file with movie data
# df = pd.read_csv('data/MovieSummaries/movie.metadata.tsv')
df = pd.read_pickle('pickles/cmu_movies_df.pkl')
freebase_ids = df['Freebase Movie ID'].tolist()

def fetch_wikidata_request(freebase_id):
  url = 'https://query.wikidata.org/sparql'
  query = f"""
    SELECT ?item ?IMDb_ID ?FreebaseID ?sitelink WHERE {{
      ?item wdt:P31 wd:Q11424 .
      ?item wdt:P646 ?FreebaseID .
      ?item wdt:P345 ?IMDb_ID .
      ?sitelink schema:about ?item ; schema:isPartOf <https://ru.wikipedia.org/> .
      FILTER(?FreebaseID = "{freebase_id}")
    }}
    """
  r = requests.get(url, params = {'format': 'json', 'query': query})
  data = r.json()
  print(data)
  return data


# def fetch_wikidata_movies():
#   query = f"""
#   SELECT ?item ?IMDb_ID ?sitelink WHERE {{
#   ?item wdt:P31 wd:Q11424 .
#   ?item wdt:P345 ?IMDb_ID .
#   ?sitelink schema:about ?item ; schema:isPartOf <https://ru.wikipedia.org/> .
#   }}
#   """

#   sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
#   sparql.setQuery(query)
#   sparql.setReturnFormat(JSON)
#   results = sparql.query().convert()
#   return results['results']['bindings']

# # Function to fetch data from Wikidata for a batch of IDs
# def fetch_wikidata_details(ids):
#   query = f"""
#   SELECT ?item ?IMDb_ID ?firebaseID ?sitelink WHERE {{
#   ?item wdt:P31 wd:Q11424 .
#   ?item wdt:P345 ?IMDb_ID .
#   ?item wdt:P2671 ?firebaseID
#   ?sitelink schema:about ?item ; schema:isPartOf <https://ru.wikipedia.org/> .
#   }}
#   """

#   endpoint_url = "https://query.wikidata.org/sparql"

#   sparql = SPARQLWrapper(endpoint_url)
#   sparql.setQuery(query)
#   sparql.setReturnFormat(JSON)

#   # Set a custom User-Agent
#   sparql.addCustomHttpHeader("User-Agent", "MyCustomUserAgent/1.0 (myemail@example.com)")

#   results = sparql.query().convert()
#   return results

# # Batch processing (e.g., 1000 IDs per request)
# # batch_size = 1000
# batch_size = 1
# all_data = []

# # for i in range(0, len(wikidata_ids), batch_size):
# for i in range(5):
#     batch_ids = freebase_ids[i:i + batch_size]
#     print('batch_ids', batch_ids)
#     batch_data = fetch_wikidata_details(batch_ids)
#     all_data.extend(batch_data)

# # Convert the results to a DataFrame and merge with the original CSV
# wikidata_df = pd.json_normalize(all_data)
# merged_df = df.merge(wikidata_df, left_on='Wikidata ID', right_on='item.value', how='left')

# # Save to a new CSV
# merged_df.to_csv('../../data/Wikidata/movies_enriched.csv', index=False)


# fetch_wikidata_movies()
wikidata = []
for freebase_id in freebase_ids[:10]:
  wikidata.append(fetch_wikidata_request(freebase_id))

print(wikidata)
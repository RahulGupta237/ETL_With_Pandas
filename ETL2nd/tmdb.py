import pandas as pd
import requests
import config
# API_KEY = config.api_key
# url = 'https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id, API_KEY)
# url='https://api.themoviedb.org/3/movie/550?api_key=a5630291947a0f581d6af19bb0581e81'
# r = requests.get(url)

############# Extract Data ####################

print("#############start Extract Data from API as JSON OR CSV OR XML etc####################")


response_list = []
API_KEY = config.api_key

for movie_id in range(550,556): 
  url = 'https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id, API_KEY)
  r = requests.get(url)
  response_list.append(r.json())

print(response_list)
df = pd.DataFrame.from_dict(response_list)
print("-----through pandas dataframe-------")



print()
print()
print()
print(df)

print()
print("##############End of EXtraction ################################")

print()
print()
print()

print("################ Start Transform ########################")
print("df columns")
print("list of columns",list(df.columns))

print()
print("categorical feature")
print()
genres_list = df['genres'].tolist()
flat_list = [item for sublist in genres_list for item in sublist]
print(flat_list)
print()


print()
print("assign one collumn general all ")

print()
result = []
for l in genres_list:
    r = []
    for d in l:
        r.append(d['name'])
    result.append(r)
df = df.assign(genres_all=result)
print(df)

print()
print("***********************************************")
print()
df_genres = pd.DataFrame.from_records(flat_list).drop_duplicates()
print()

print(df_genres)

print()
print("***Df_target columns******")
print()
df_columns = ['budget', 'id', 'imdb_id', 'original_title', 'release_date', 'revenue', 'runtime']
df_genre_columns = df_genres['name'].to_list()
df_columns.extend(df_genre_columns)
print(df_columns)
print()
print("********explode*******")
s = df['genres_all'].explode()
print(s)
print()
print("***********Join Operations***********")
print()
df = df.join(pd.crosstab(s.index, s))

print(df[df_columns].tail(12))
if df[df_columns].isnull().sum().sum()==0:
  print("Null value not present")
else:
  print(df[df_columns].isnull().sum().sum())

#--------------------------------------------------------------------------

df['release_date'] = pd.to_datetime(df['release_date'])
df['day'] = df['release_date'].dt.day
df['month'] = df['release_date'].dt.month
df['year'] = df['release_date'].dt.year
df['day_of_week'] = df['release_date'].dt.day_name()
df_time_columns = ['id', 'release_date', 'day', 'month', 'year', 'day_of_week']


print(df[df_time_columns])
# check null value
if df[df_time_columns].isnull().sum().sum()==0:
  print("Null value not present")
else:
  print(df[df_time_columns].isnull().sum().sum())


print(type(df[df_time_columns]))


print()
print()
print()
print("################### End Transformations ###############")
########################LOAD DATA TO CSV FILES#######################################################
print()
print()
print()
print("################### Load Data as CSV or other DB ###############")
print()
print()
print(df.count())

data_types = pd.DataFrame(df.dtypes, columns=['data_type'])
print("hhhhhhhhhhhhhhhhhhhhhhhhhhh")
data_types['missing'] = round(((len(df)-df.count())/(len(df)))*100,2)
print(data_types['missing'])
# card = [df[col].nunique() for col in df.columns]
# print(card)

# print()
# df[df_columns].to_csv('tmdb_movies.csv', index=False)
# df_genres.to_csv('tmdb_genres.csv', index=False)
# df[df_time_columns].to_csv('tmdb_datetimes.csv', index=False)

print()
print()
print()
print("################### End Load ###############")

import data_quality as q
x=q.dqr(df[df_columns])
print(x)

"""


"""




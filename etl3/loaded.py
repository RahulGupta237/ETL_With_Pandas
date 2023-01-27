import pandas as pd

# df[df_columns].to_csv('tmdb_movies.csv', index=False)
# df_genres.to_csv('tmdb_genres.csv', index=False)
# df[df_time_columns].to_csv('tmdb_datetimes.csv', index=False)


def join(data1,data2):
    newdata=pd.merge(data1,data2, left_index=True, right_index=True)

    
    return load(newdata)


def load(data_warehouse):

    data_warehouse.to_csv("newtarget_data.csv")
    print("data successfully loaded")
    print()
    print()
    print(data_warehouse)
import pandas as pd
import numpy as np
from functools import reduce


# 1. Drop Rows with Null Columns
def drop_nulls(df, cols):
  df.dropna(subset = cols, inplace=True)
  return df

# 2. Fill Null Columns with Av Values 
def fill_vals(df, cols):
 for i in cols:
   av = df[i].mean()
   df[i].fillna(av, inplace = True)
 return df

# 3. Replace Strings with numbers and convert type
def replace_strings(df, cols):
  for i in cols:
    df[i].replace('3+',4, inplace = True)
    df[i] = pd.to_numeric(df[i])
  return df

def data_clean_loan(df):

    if df.isna().sum().sum()== 0:
        print("data already cleaned")

    else:
        col_having_nan_values=df.loc[:, df.isnull().any()].columns
        print(col_having_nan_values)
        #df['Dependents'].value_counts()
        list_of_column_Nan_value=list(col_having_nan_values)
        av_cols = ['LoanAmount']
        rp_cols = ['Dependents']

        df = df.pipe(drop_nulls,list_of_column_Nan_value).pipe(fill_vals,av_cols).pipe(replace_strings, rp_cols)

    # verifiying data
    if df.isnull().sum().sum()==0:
        print("successfully handled missing data",0)
        print(df)


def clead_data_book(df):
    if df.empty:
        print("have a empty value")
    else:
        print("No empty value")
    if df.isna().sum().sum()== 0:
        print("data already cleaned")

    else:
        col_having_nan_values=df.loc[:, df.isnull().any()].columns
        print(col_having_nan_values)
        #df['Dependents'].value_counts()
        list_of_column_Nan_value=list(col_having_nan_values)
        print(list_of_column_Nan_value)
        df.drop(list_of_column_Nan_value, inplace = True, axis = 1)
        print(df.shape)
        print(df)
def habdle_duplicate(df):
    if df.duplicated().sum().sum()==0:
        print("here no duplicate value")
    else:
        print("duplicate value occur")
        print("print duplicate row")
        print("i am duplicated",df[df.duplicated(keep=False)])
        df.drop_duplicates()
    


# import Extract
# # df=Extract.readdata("loan.csv")
# # data_clean(df)
# df=Extract.readdata("Images-Book.csv")
# print(df.shape)
# print(df.isnull().values.sum())
# habdle_duplicate(df)
# clead_data_book(df)
# print(df.isnull().values.sum())
# habdle_duplicate(df)

# targt=df[df.columns[4:]]
# print(targt)




     

import Extract,transform,loaded
# df=Extract.readdata("loan.csv")
# data_clean(df)

print("**********Extraction***************")
loan_data=Extract.readdata("loan.csv")
book_data=Extract.readdata("Images-Book.csv")

print("** Transform***********")
print()

print(loan_data.shape)
print(loan_data.isnull().values.sum())
data1=transform.data_clean_loan(loan_data)
data1=transform.habdle_duplicate(loan_data)
data2=transform.clead_data_book(book_data)
data2=transform.habdle_duplicate(book_data)

print(data1)
print(data2)
print(loan_data.index)
print(book_data.index)

print("******Loading the data*******")

data1o=loan_data[loan_data.columns[4:]]

data2o=book_data[book_data.columns[4:]]

load=loaded.join(data1o,data2o)
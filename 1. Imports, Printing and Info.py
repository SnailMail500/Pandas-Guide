#Imports, Printing and Info using pandas
import pandas
import pyarrow
import math


print(pandas.options.display.max_rows)#prints the maximum number of rows that can be printed without a to_string()
#method


weatherData = pandas.read_csv("C:/Users/Admin/Desktop/Pandas LDS Test/LDS/all-stations-uk.csv")

print(weatherData.info())#shows info about the data

#now you're familiar with imports, printing the data and info about the data, go and do:
#Data Cleaning
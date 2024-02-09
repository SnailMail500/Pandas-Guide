#Data Cleaning using pandas

#Data Cleaning is the practice of fixing bad data, e.g:
#Empty cells, wrong format, wrong data or duplicates

import pandas
import math
weatherData = pandas.read_csv("C:/Users/Admin/Desktop/Pandas LDS Test/LDS/all-stations-uk_LIVE.csv")
#Using a premade live copy so it doesn't get messed up since the csv file might get changed
#if needed, can always make a new live copy of the original copy

#Cleaning empty cells:

weatherData.dropna()#this will make a new frame and do changes there- if you want to save to the live document, you can:
#do this:
#weatherData.dropna(inplace = True)

print(weatherData.to_string())

#if, for reasons unknown to me, you want to fill in the null values, use:
#df.fillna(value)
#if needing to work on the live document and not on a temp frame, the second argument must be:
#inplace = True

#if you want to replace null vals in only one column, you can do:
#weatherData["Daily Mean"].fillna(13)
#args same as normal if using inPlace

#or you can get pandas to calc a central measure of tendancy and replace null values with that
#which is better than using a random value for obvious reasons#
#x = weatherData["Daily Mean"].mean#this takes the mean of the daily mean column and I'm really regretting using that specific column
#replace .mean with .mode or .median methods to calculate other CMTs if they are better for the specific data

#Cleaning data of the wrong format:

#for example

#weatherData["Date"] = pandas.to_datetime(weatherData["Date"])
#if there is badly formatted data in the date column which needs to be cleaned into the date time format
#as long as the data is mm/dd/yy or the like.
#or, if there are NULLs in the date column:

weatherData.dropna(subset = ["Date"])#get rid of all nulls of the subset "Date"

#which will drop all Nulls in the "Date" column

#Cleaning wrong data:

#wrong data is not necessarily empty or in the wrong format
#it can just be plain wrong, like if the data is 199, instead of 1.99
#wrong, but errors like this are ususally spottable in smaller data sets

#because this data set is of a decent size (it's not actually big data, it's fairly small, but has some volume and veracity.
#this data has no velocity- it is static (there is no feed of data))
#anyway, because the data is of a decent size, we should set rules for going through it and replacing wrong data.
#like this:

#for x in weatherData.index:
#    if weatherData.loc[x, "Daily Mean"] == "n/a":
#        weatherData.loc[x, "Daily Mean"] = 0

#print("Replaced all values equal to \"n/a\" in the column \"Daily Mean\" with \"0\".")
#etc...
#so if any values in daily mean = n/a (there was no rain or whatever), it will replace them with 0- which is much better
#because otherwise it will throw a wobbly, you can't calculate a mean if some of the values are n/a

#in fact, this might be a good idea for the whole dataset, depending on what it's like.

#or, you can just assume that the rows with incorrect data are discardible although this sounds a bit stupid
#but maybe it's what the data needs.

#so:

#for x in weatherData.index:
#   if weatherData.loc[x, "Daily Mean"] > 90:
#       weatherData.drop(x)
#for every row in "Daily Mean", if the value > 90, drop it
#this will definitely affect accuracy, so the code is commented out. try it if you want, it's your life and you have a copy of the
#original file.

#Duplicate rows:

print("Duplicate? ")
print(weatherData.duplicated)#this will send a boolean result back for each row
#no duplicates as printed data. Good.
#Finding Correlations using pandas

import pandas

weatherData = pandas.read_csv("C:/Users/Admin/Desktop/Pandas LDS Test/LDS/all-stations-uk_LIVE.csv")

weatherData.dropna()
weatherData.drop('Date', axis = 1)#need to get rid of the date for the frame in this case
#i believe it is cause it's a british format and pandas therefore won't recognise it as
#a date- and changing every date is honestly too much effort. Only working on live frame
#so no need to worry about deleting every date in the actual file.
#the axis must be 1 here as default axis = 0 which is for the rows.

#we know there are no duplicates in this file- look at 2. Data Cleaning to see why.

#corr() is actually a great bit of pandas and a good part of why I'm using it
#it can calculate correlations between each column

weatherData.corr()
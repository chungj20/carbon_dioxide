import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy.optimize import curve_fit

def oscFunc(x, amp, period, offset):  
    return amp/2 * np.cos((x + offset)  * 2 * np.pi/period) 

def plyFunc(x,c0,c1,c2):
    return c0+x*c1+x**2*c2

dfCarbonDioxide=pd.read_table('co2_mlo.txt',delimiter=r"\s+",skiprows=146)
dfCarbonDioxide['date']=pd.to_datetime(dfCarbonDioxide[['year', 'month', 'day', 'hour', 'minute', 'second']])
boolMissing=dfCarbonDioxide['value']==-999.99
dfCarbonDioxide[boolMissing]=np.nan
dfCarbonDioxide=dfCarbonDioxide.dropna()
dfCarbonDioxide=dfCarbonDioxide.reset_index(drop=True)
print(dfCarbonDioxide)

fig, ax = plt.subplots(figsize=(12,8))
ax.plot(dfCarbonDioxide['date'],dfCarbonDioxide['value'],'ok')
ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')

startDate=min(dfCarbonDioxide['date'])
timeElapsed=dfCarbonDioxide['date']-startDate
daysSinceStart=timeElapsed.dt.days
#have feature that allows for scipy to calculate linear growth 

Curvefit=np.polyfit(daysSinceStart, dfCarbonDioxide['value'],2)
print(Curvefit)

fig,axResidual=plt.subplot()
ax.Residual(dfCarbonDioxide['date'],dfCarbonDioxide['value'],'ok')

predicted=plyFunc(daysSinceStart,[2],[1],[0])

#first create polynomial fit and then subtract that from the original data to see what is left
#keep doing this to improve the fit to the data
#use scipy to do this, but try with numpy first


#have sine or cosine wave that accounts for the up and down of the CO2 levels


#^this line of code converted the pandas series, convert it to the floating point number of days
#daysSinceStart IS our x variable, now it's time for you to plug in and create y

#code below should help -- it isn't complete -- with making the cosine aspect of the wave
#def oscFunc(x, amp, period, offset):  
#    return amp/2 * np.cos((x + offset)  * 2 * np.pi/period) 
#365 days 

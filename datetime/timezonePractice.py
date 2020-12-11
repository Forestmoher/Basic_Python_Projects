#Author Forest Moher

#Python Version: 3.9.0

#Purpose Create a class structure for a company with branches in different locations, and determine if they
#are open based on their local time


import datetime as dt
import pytz

#print(pytz.timezone('US/Pacific'))

#local = time.localtime()
#print(time.strftime("%H:%M",local))

class branch:

    def __init__(self,Name,Timezone):
        self.Name = Name
        self.Timezone = Timezone

        #this function will check the time zone attr. of the opject to
        #see if it is open. 
        def isOpen(Timezone):
            hours = (9,10,11,12,13,14,15,16)
            currentTime = dt.datetime.now(pytz.timezone(Timezone))
            if currentTime.hour in hours:
                return "Open"
            else:
                return "Closed"
            
        self.Open = isOpen(Timezone)
        #this attr. is simply for displaying the time to the user
        self.curtime = dt.datetime.now(pytz.timezone(Timezone)).strftime('%H:%M')

           
#create three objects, one for each branch
pdx = branch("Portland",'US/Pacific')
nyc = branch("New York",'US/Eastern')
lon = branch("London","Europe/London")


print("Current time in \nPortland: {}\nNew York: {} \nLondon: {}".format(pdx.curtime,nyc.curtime,lon.curtime))
print("Portland: {}\nNew York: {}\nLondon: {}".format(pdx.Open,nyc.Open,lon.Open))
        

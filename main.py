import os
import sys

def anchor(year):
    c = year / 100
    d = 5 * (c % 4) % 7 + 2
    #return parseDay(str(d))
    return d
        
def parseDay(day):
    pd = {"0" : "Sunday",
          "1" : "Monday",
          "2" : "Tuesday",
          "3" : "Wednesday",
          "4" : "Thursday",
          "5" : "Friday",
          "6" : "Saturday",
          "7" : "Sunday"}
         
    return pd[day]
        
def doomsday(month, year=2017):
    dd = {"3" : 14,
          "4" : 4,
          "5" : 9,
          "6" : 6,
          "7" : 11,
          "8" : 8,
          "9" : 5,
          "10" : 10,
          "11" : 7,
          "12" : 12}
        
    isLeap = leap(year)
    if isLeap:
        dd["1"] = 4
        dd["2"] = 29
    else:
        dd["1"] = 3
        dd["2"] = 28
    return dd[month]
        
def leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        
def odd(i):
        return i % 2
        
def parseYear(year):
    return int(str(year)[2] + str(year)[3])
        
def date(month, day, year):
    # TODO
        
        

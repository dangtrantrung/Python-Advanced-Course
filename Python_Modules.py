result=min(2,3,4)
print(result)
result1=max(-1,2,3,-7,4,-5)
print(result1)
result2=max(2,-3,min(4,7),-5)
print(result2)
result3=min(max(3,4),abs(-5))
print(result3)
result4=abs(min(4,6,max(2,8)))
print(result4)
result5=round(max(5.572,3.258),abs(-2))
print(result5)

def func1 (args):
    pass
def Tripple(num):
    return num*3
print(Tripple(5))

def absolute_differences(num1,num2):
    return abs(num1-num2)
print(absolute_differences(5,6))
def km_to_miles(km):
    return km/1.6
print(km_to_miles(5))

def average_grade(grade1,grade2,grade3):
    return round((grade1+grade2+grade3)/3,1)
print(average_grade(80,95,90))

def top_three_avg(grade1,grade2,grade3,grade4):
    total=grade1+grade2+grade3+grade4
    top_three=total-min(grade1,grade2,grade3,grade4)
    return round(top_three/3,1)
print(top_three_avg(50,60,70,80)) #70

def week_elapsed(day1,day2):
    return(int(abs(day1-day2)/7))

print(week_elapsed(3,20))
print(week_elapsed(20,3))
print(week_elapsed(8,5))
print(week_elapsed(40,61))

import math

print (math.floor(-2.8))
print(abs(round(-4.3)))
print(math.ceil(math.sin(34.5)))

import calendar

print(calendar.isleap(2021))
print(calendar.leapdays(2000,2050))
print(calendar.weekday(1982,10,9))
print(help(calendar.isleap))
print(dir(calendar))
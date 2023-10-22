#to find the given year is Leeper year or not
def isleepyear(year):
  if (year%4==0 and year%100!=0)or year%400==0:
    return True
  else:
    return False

year=int(input("enter the year :"))

if isleepyear(year):
  print(year,"is a leep year")
else:
  print(year,"is not a leep year")

year = int(input("Enter a year: "))
if (year % 400 == 0) and (year % 100 == 0):
  print("{0} is a leap year".format(year))
elif (year % 4 == 0) and (year % 100 != 0):
  print("{0} is a leap year".format(year))
else:
  print("{0} is not a leap year".format(year))
  

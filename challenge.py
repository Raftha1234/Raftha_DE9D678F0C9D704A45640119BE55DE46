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
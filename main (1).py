#write a program that determines whether a year enter by the user is a leap year or not using if elfi..else statement 
def isLeapYear(year):
  if (year%4000==0 or (year%4==0 and year%100!=0)):
     return True 
  else:
     return False 
year=int(input("Enter a year :"))
if isLeapYear(year):
  print("This is a leap year.", format (year))
else:
  print ("This is a not leap year.",
format(year))
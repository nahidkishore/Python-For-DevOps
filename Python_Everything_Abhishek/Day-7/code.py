import sys
type=sys.argv[1]
if type=="t2.micro":
  print("It will charge you 2 dollors per day")

elif type=="t2.medium":
  print("It will charge you 4 dollors per day")

elif type=="t2.large":
  print("It will charge you 8 dollors per day")
    
else:
  print("Please provide a valid instances type")  
import sys
type=sys.argv[1]
if type=="t2.micro":
  print("ok, we will create a t2 micro instances for you")

elif type=="t2.medium":
  print("ok, we will create a t2 medium instances for you")
else:
  print("nothing bro")  
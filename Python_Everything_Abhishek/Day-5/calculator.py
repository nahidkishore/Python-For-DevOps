import sys

def add (num1, num2):
  a=num1 + num2
  return a

def mul (num1, num2):
  m=num1 * num2
  return m

def div (num1, num2):
  d=num1 / num2
  return d

num1=int(sys.argv[1])
operation=sys.argv[2]
num2=int(sys.argv[3])


if operation =="add":
  output = add(num1, num2)
  print(output)
  
if operation =="mul":
  output = mul(num1, num2)
  print(output)

if operation =="div":
  output = div(num1, num2)
  print(output)  
  
  

# python3 calculator.py 2 add 3  
# python3 calculator.py 2 mul 3
# python3 calculator.py 10 div 2
  
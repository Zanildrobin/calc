import math
import decimal

def efinder(e):
  d = 2  
  for i in range(2, e):
    d = decimal.Decimal(d + (decimal.Decimal(1/math.factorial(i))))
  print(d)
  
inp = int(input())
efinder(inp)
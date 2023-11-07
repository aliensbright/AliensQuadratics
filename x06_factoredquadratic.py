#!python3
'''
This is a challenging problem!

x06. Determine the factored form
You may use the functions you created in previous assignments
'''
from x01_discriminant import discriminant
import math
def Factored(a,b,c):
  dis=discriminant(a,b,c)
  if dis<0:
    return None
  else:
    root1=(-b+math.sqrt(dis))/(2*a)
    root1=round(root1)
    if root1>0:
      factor1=f'(x - {root1})'
    else:
      factor1=f'(x + {-root1})'
    
    root2=(-b-math.sqrt(dis))/(2*a)
    root2=round(root2)
    if root2>0:
      factor2=f'(x - {root2})'
    else:
      factor2=f'(x + {-root2})'
    factors=[factor1,factor2]
    print(factors)
    return factors


'''
input parameters:
a, b, c: signed float
These are the coefficients in the quadratic function ax^2 + bx + c = 0

Write the equation in a nicely formatted factored form. This means no fractions

return:
list : 2 string literals representing the factors.  The order does not matter
None if the quadratic can not be factored
'''

def main():
  assert "(x + 3)" in Factored(1,1,-6) == True
  assert "(x - 2)" in Factored(1,1,-6) == True
  assert "(x + 2)" in Factored(1,7,10) == True
  assert "(2x + 1)" in Factored(2,5,2) == True
  assert "(x + 2)" in Factored(2,5,2) == True
  assert "(3x + 1)" in Factored(6,-7,-3) == True
  assert Factored(1,4,7) == None
  assert Factored(2,4,4) == None
 
if __name__ == "__main__":
  main()
 
import sys
import math
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
x1= (-b+math.sqrt(b*b-4*a*c))/2*a
x2= (-b-math.sqrt(b*b-4*a*c))/2*a
print( f"{int(x1)}")
print( f"{int(x2)}")
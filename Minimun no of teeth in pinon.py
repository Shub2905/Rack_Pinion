
import math

import numpy as np



A = float(input("Enter Addendum "))


m = float(input("Enter Module "))


Pa = float(input("Enter Pressure Angle "))



T= (2*A)/(m*np.sin(Pa) ** 2)


print (T)


# lucas 20  is 15127 - computed in 0.0 seconds
# >>> my_problem_3(992, 999)
# lucas 992 is 206889822962565451392887592453927820360548298860512831381912829148503279112793457719085839841935860743415404025848133822882266210
# 9930138906174281640854190975242654915590857142335925799894132933093849658570047 - computed with 992 calls in 0.0 seconds

# Problem 3:  (1 point).
# Instead of returning just two values from each call to Lucas-- i.e., the computed Lucas value Lk,
# together with the number of procedure calls required to do the computation-- return three:
# •	The computed Lucas value,  Lk
# •	The computed Lucas value before that value,   Lk-1
# •	The number of procedure calls required to compute that result
# Handle the two base cases as follows:
# •	For  L0,  return  L0 = 2, L-1 = null, procedure calls = 1
# •	For  L1,  return  L1 = 1, L0 = 2, procedure calls = 1
# For the general case, you can compute  Lk  by invoking Lucas on k-1, then adding   Lk-1   and     Lk-2
# Run this code twice:
# •	Once to compute L0 … L20
# •	Again, for a range of Lucas values that either (a) requires a measureable amount of time to run -
#ideally, at little more than 1 second, or (b) causes a runtime failure somewhere in the middle of that range.

import time
import sys

def lucas():

    if (k==0):

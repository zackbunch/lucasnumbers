# Problem 2b:  (2 point).

# Inside of your problem 1 Lucas function, define a nested, helper function that does the following:
# •	accepts 1 argument - the index of the Lucas number to compute
# •	recursively computes this value and counts the number of function calls as before, once again using the
# timeout parameter to limit its runtime
# •	on success, returning the Lucas number and the number of function calls, as before.

# Your outer Lucas function should
# •	check the preconditions on the index of the Lucas number and the timeout value, as before, then
# •	call the nested, helper function with the index of the Lucas number
# •	returning the value that this helper function returns
#

import time
import sys
import  datetime


timesCalled = 0

maxTimeout = 2

def lucas(k,t,maxTimeout):


    # Error handling
    if not isinstance(k, int):
        raise TypeError("Sorry.{} is not an integer.".format(k))
    if not k >= 0:
        raise ValueError("Sorry. {} must be zero or positive.".format(k))

    # if (time.time() - t > maxTimeout):
    #
    #     sys.exit()


    def inner_lucas(k): #accepts one argument - the index of the lucas number to compute


        maxTimeout = 2
        lucas.counter +=1
        if (k == 0):
            return 2
        elif (k == 1):
            return 1
        elif(k >= 2):


            return inner_lucas(k-1) + inner_lucas(k-2)



    for i in range(k+1):
        start = time.time()
        _inner_lucas = inner_lucas(i)
        end = time.time()
        finish = end - start
        if finish > maxTimeout:
            sys.exit("timeout at lucas {} after 120 seconds".format(i))
        elif finish < maxTimeout:
            print('lucas {} is {} - computed with {} calls in {:.4f} seconds'.format(i,_inner_lucas,lucas.counter,finish))
            lucas.counter = 0

    return inner_lucas(k)







# driver code
lucas.counter = 0
lucas(35,time.time(),2)

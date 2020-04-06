# Instead of implementing the start time and maximum wall clock time values as
# parameters to the Lucas function, make them write-once globals to the Lucas function,
# This will reduce the number of parameters the function accepts to 1.

import time
import sys
#global variables
maxTimeout = 2
timesCalled = 0
start = time.time()
def lucas(k):
    global maxTimeout
    global start
    global timesCalled


    if not isinstance(k,int):
        raise TypeError("Sorry. {} is not an integer.".format(k))
    if not (k >= 0):
        raise ValueError("Sorry. {} must be greater than or equal to zero.".format(k))

    timesCalled = timesCalled + 1

    maxTimeout = 2
    if (k == 0):
        return 2
    elif (k == 1):
        return 1
    elif(k >= 2):
        return lucas(k-1)+lucas(k-2)


def callLucas(howMany):
    global maxTimeout
    global start
    global timesCalled

    for i in range(howMany+1):
        start = time.time()
        _lucas = lucas(i)
        finish = time.time()
        if (finish - start > maxTimeout):
            sys.exit("timeout at lucas {} after 120 seconds".format(i))
        else:
            print('lucas {} is {} - completed with {} calls in {:.4f} seconds'.format(i, _lucas,timesCalled,finish-start))
            timesCalled = 0


callLucas(38)

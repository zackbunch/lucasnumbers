import time
import sys
maxTimeout = 2
timesCalled = 0



def lucas(k, t,maxTimeout=2):

    if (time.time() - t > maxTimeout):

        raise Exception()


    global timesCalled
    timesCalled = timesCalled + 1
    if (k == 0):
        return 2
    elif (k == 1):
        return 1
    elif(k >= 2):
        return lucas(k - 1, t,maxTimeout) + lucas(k - 2, t,maxTimeout)

# lucas 36 is 33385282 - computed with 48315633 calls in 98.742647 seconds
# timeout at lucas 37 after 120 seconds


def callLucas(howMany):
    start = time.time()
    global timesCalled
    for i in range(howMany+1):
        try:
            _lucas = lucas(i, start,maxTimeout)
            finish = time.time()
            print("lucas {} is {} - computed with {} calls in  {} seconds".format(
                i, _lucas, timesCalled, finish-start))
            timesCalled = 0
        except Exception as ex:
            # print(str(ex))
            sys.exit("timeout at lucas {} after 120 seconds".format(i))


callLucas(50)

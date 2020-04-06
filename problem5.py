# Problem 5:  (2 points).
# Recode your Lucas function one last time,
# •	using the standard "closed form" formula (look it up), rather than loops and/or recursive calls to compute the values
# •	eliminating the timeout check.
# Since this formula involves the use of a square root, you'll need to round off your results to make them precise, In your client code, display
# both the "raw" value returned by your Lucas function and the rounded value, along with the number of digits in the rounded value.


#
# >>> my_problem_5(0,21)
# lucas 0 is 2.0 -- i.e., 2 -- with 1 digits
# lucas 1 is 1.0 -- i.e., 1 -- with 1 digits
# lucas 2 is 3.0 -- i.e., 3 -- with 1 digits
# lucas 3 is 4.0 -- i.e., 4 -- with 1 digits
# lucas 4 is 7.000000000000001 -- i.e., 7 -- with 1 digits
# lucas 5 is 11.000000000000002 -- i.e., 11 -- with 2 digits
# lucas 6 is 18.000000000000004 -- i.e., 18 -- with 2 digits
# lucas 7 is 29.000000000000007 -- i.e., 29 -- with 2 digits


def lucas(k):
    sqrt5 = pow(5,0.5)
    term1, term2 = (1+sqrt5)/2,(1-sqrt5)/2
    return pow(term1,k)+pow(term2,k)


def callLucas(x,howMany):

    for i in range(x,howMany+1):
        _lucas = lucas(i)
        roundedLucas = int(round(_lucas))
        number = roundedLucas
        count = 0
        while (number > 0):
            number = number//10
            count = count +1
        print('lucas {} is {} -- i.e., {} -- with {} digits'.format(i,_lucas,roundedLucas,count))


callLucas(8,20)
# callLucas(1470,1480)

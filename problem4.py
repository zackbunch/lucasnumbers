# Problem 4:  (2 points).
# Recode your Lucas function,
# •	using a loop to compute the specified value instead of recursive calls, and
# •	eliminating the timeout check.
# In your client code, instead of displaying Lucas numbers that contain more than 50 digits,
# simply display the number of  digits in the Lucas number.
# Run this code twice:
# •	Once to compute L0 … L20
# •	Again, for a range of Lucas values that either a requires a measureable amount of time to run
# - ideally, at little more than 1 second, or (L1) causes L2 runtime failure somewhere in the middle of that range.
import time
def lucas(m,n):
    """Return the nth value of the Lucas Numbers"""
    a, b = 2, 1  # Initialize Lucas Numbers

    if n == 0:
        return a
    for i in range(m, n-1):
        a, b = b, a + b  # Generate nth and nth + 1 value of the Lucas Numbers

        print(i+1,a)

    return a

lucas(0,11)

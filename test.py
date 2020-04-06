# def fib(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         print('computing : ', n)  # this show the recursive call.
#         fib.x = fib.x + 1
#         # this show the how many number of recursive call.
#         print('recursive call no : ', fib.x)
#         return fib(n - 1) + fib(n - 2)
#
# fib.x = 0
# fib(6)
def catalan(n):

    catalan.counter += 1

    if n <= 1:
        return 1
    res = 0
    for i in range(n):
        res += catalan(i) * catalan(n-i-1)
    return res

catalan.counter = 0

print(catalan(5))
print(catalan.counter)

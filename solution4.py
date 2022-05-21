# Write code for algorithm 4 below
def power(a,b):
    # base case 
    # if b == 1
    # return a
    if b == 1:
        return a
    # else a * power(a, b - 1) 
    else:
        return a * power(a, b - 1)
print(power(8, 20))
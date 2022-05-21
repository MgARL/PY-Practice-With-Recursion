# Write code for algorithm 3 below
def fibo_Sequence(n):
    # base case
    if n <= 1:
        return n
    else:
        return (fibo_Sequence(n-1) + fibo_Sequence(n-2))

print(fibo_Sequence(5))
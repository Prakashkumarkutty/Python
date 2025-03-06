#  N-th term of Arithmetic Progression

# a - first element 
# d - difference 
# n - nth term
def N_thTerm(a,d,N):
    nThTerm = a
    for i in range(1,N):
        nThTerm +=d
    return nThTerm

result = N_thTerm(12,2,4)

print("Answer is ",result)
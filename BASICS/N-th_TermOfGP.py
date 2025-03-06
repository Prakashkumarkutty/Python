# Nth term of given Geometric Progression

# a - initial 
# r - times
# N - Nth place

def N_th_TermOfGP(a,r,N):
    nthTerm = a
    for i in range(1,N):
        nthTerm *= r

    return nthTerm

result = N_th_TermOfGP(67,381,236)
print(result)
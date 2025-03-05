def sumNaturals(N):
    total = 0
    for i in range(N+1): #range start from 0 
        total = total + i  
    return total

result = sumNaturals(3)

print("Output",result)
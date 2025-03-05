def MultiplicationTable(n,i=1):
    if(i==11):
        return
    print(n," *", i , " =" ,n*i)
    i +=1
    MultiplicationTable(n,i)

result = MultiplicationTable(3)

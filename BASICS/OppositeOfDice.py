# # Naive Approach

# def diceProblem(n):
#     if(n>6):
#         return "Enter only a number between 1 to 6"
    
#     if(n==1):
#         return 6
#     elif(n==2):
#         return 5
#     elif(n==3):
#         return 4
#     elif(n==4):
#         return 3
#     elif(n==5):
#         return 2
#     else:
#         return 1
    
# result = diceProblem(1)
# print(result)


# Best approach

def oppositeOfDice(n):
    ans = 7 -n     # TOTAL posibility is 6 so we can get opposite using subtract from 7

    print(ans)

oppositeOfDice(2)
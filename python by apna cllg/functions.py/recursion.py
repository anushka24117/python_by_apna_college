#recursive function
# def show(n):
#     if (n==0):  #base case
#         return
#     print(n)
#     show(n-1)

# show(5)

# def show(n):
#     if (n==0):  #base case
#         return
#     print(n)
#     show(n-1)
#     print("end")

# show(3)


# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     return fact(n-1)*n

# print(fact(5))



# def cal_sum(n):
#     if (n==0 ):
#         return 0
#     return cal_sum(n-1)+n

# sum=cal_sum(5)
# print(sum)


fruits=["mango","litchi","apple","banana"]
def print_list(list,idx=0):
    if(idx==len(list)):
        return 
    print(list[idx])
    print_list(list,idx+1)

print_list(fruits)
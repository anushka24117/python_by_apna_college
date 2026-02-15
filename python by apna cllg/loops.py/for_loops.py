#Syntax 
# for el in list:
    #some work


#To print list using for loops
# list=[1,2,3]
# for el in list:
#     print(el)

# nums=[1,2,3,4,5]
# for val in nums:
#     print(val)


#To print str using for loop
# veggies=["potato","brinjal","ladyfinger","cucumber"]
# for val in veggies:
#     print(val)

#To print tuple using for loop
# tup=(1,2,3,4,2,8,9)
# for el in tup:
#     print(el)

#To print str using foor loop
# str=("apnacllg")
# for ch in str:
#     print(ch)


#For loop with else
# str="apnacllg"
# for ch in str:
#     print(ch)
# else:
#     print("end")   #a  p n a c l l  g  end   <- output



# str="apnacollege"
# for ch in str:
#     if(ch=='o'):
#         print("o found")
#         break
#     print(ch)
# else:
#     print("end")       a p n a c o found


# str="apnacollege"
# for ch in str:
#     if(ch=='o'):
#         print("o found")
#         break
#     print(ch)

# print("end")              # a p n a c o found end


#practice questions using for loop
# nums=[1,4,9,16,25,36,49,64,81,100]
# for el in nums:
#     print(el)



# nums=[1,4,9,16,25,36,49,64,81,100]      
# x=int(input("enter number: "))
# idx=0
# for el in nums:
#     if(el==x):
#         print("x found at idx",idx)
#     idx+=1

# nums=[1,4,9,16,25,36,49,64,81,100]
# x=int(input("enter number: "))
# idx=0
# for el in nums:
#     if(el==x):
#         print("x found at idx",idx)
#         break
#     idx+=1

#range and pass function in python
# for el in range(5):
#     print(el)         #0 to 4

# for el in range(1,5):   #1 to 4
#     print(el)

# for el in range(1,5,2):   #1,3
#     print(el)

# print(range(5))    #range(0, 5)


# seq=range(5)
# print(seq[0])    #0
# print(seq[1])    #1
# print(seq[2])     #2
# print(seq[3])     #3
# print(seq[4])     #4
# print(seq[5])    #error


# seq=range(5)
# for i in seq:
#     print(i)   #o to 4

# for i in range(10):   #stop value only
#     print(i)         #0 to 9 

# for i in range(2,10):   # range(start,stop )value only
#     print(i)         #2 to 9 

# for i in range(2,10,2):   # range(start,stop,step )value 
#     print(i)         #2 4 6 8 

#To print even numbers from 2 to 100
# for i in range(2,101,2):   # range(start,stop,step )value
#     print(i)

#To print odd numbers from 1 to 100
# for i in range(1,100,2):   # range(start,stop,step )value
#     print(i)









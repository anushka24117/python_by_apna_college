# nums={1,2,3,4}
# set2={1,2,2,2}  #{1,2}
# print(nums)
# print(set2)

# collection={1,2,3,4}
# print(collection)
# print(type(collection))

# collection={1,2,3,4,"hello","world"}   #str can also be printed 
# print(collection)
# print(type(collection))   #ouput has no order of execution ->unordered output


# collection={1,2,3,4,"hello","world","world"}   #ignores double values and reduced to one with no error
# print(collection)
# print(len(collection))  # 6 ignores duplicate values 

#To create empty set
# collection=set()
# print(type(collection))


#Set Methods
# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(2)
# print(collection)   #{1,2}



# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(2)
# collection.remove(1)
# print(collection)      #{2}


# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(2)
# collection.remove(1)
# collection.remove(7)   #error
# print(collection)      


# collection=set() #null set created
# collection.add(1)
# collection.add(2)
# collection.add("apnacllg")
# collection.add((1,2,3))
# print(collection)   #{1,2,'apnacllg',(1,2,3)}


# collection=set() #null set created
# collection.add(1)
# collection.add(2)
# collection.add("apnacllg")
# collection.add((1,2,3)) 
# collection.clear()
# print(len(collection))  #0


#unhashable ( whose values can be changed) 
# collection=set()
# collection.add([1,2,3])
# print(collection)


# collection=set() #null set created
# collection.add(1)
# collection.add(2)
# collection.add("apnacllg")
# collection.add((1,2,3)) 
# print(collection)
# print(len(collection))   #4


# collection={"hello","apnacllg","world","coding","python"}
# print(collection.pop())
# print(collection.pop())
# print(collection.pop())   #picks random values 


#union in set
# set1={1,2,3}
# set2={2,3,4}
# print(set1.union(set2))  #{1,2,3,4}
# print(set1)              #{1,2,3}
# print(set2)              #{2,3,4}


#Intersection in set
# set1={1,2,3}
# set2={2,3,4}
# print(set1.intersection(set2))   #{2,3}


#Practice Question1
# dict={
#     "table":("a piece of furniture","list of fact & figures"),
#     "cat":"a small animal",
# }
# print(dict)   #{'table': ('a piece of furniture', 'list of fact & figures'), 'cat': 'a small animal'}

#Practice Question 2 

# subjects = {
#     "python","java","c++","python","javascript","java","python","java","python","java","C++","c"
# }
# print(subjects)  #C++ & c++ are treated different  so {'python', 'c', 'C++', 'c++', 'javascript', 'java'} 
# print(len(subjects))     #output 6


# subjects = {
#     "python","java","c++","python","javascript","java","python","java","python","java","c++","c"
# }
# print(subjects)            #{'c++', 'c', 'javascript', 'python', 'java'}
# print(len(subjects))       #5

#Practice Question 3
# x=int(input("enter physics marks: "))
# y=int(input("enter chemistry marks: "))
# z=int(input("enter maths marks: "))

# marks={}
# marks.update({"phy":x})
# marks.update({"chem":y})
# marks.update({"maths":z})

# print(marks)


#Practice Question 4
# values={9,9.25,8,8.0}
# print(values)           #{8, 9, 9.25} ignored 8.0

# values={9,"9.0"}
# print(values)    # {9, '9.0'} stored in the form of string 


values={    #stored in the form of set
    ("float",9.0),
    ("int",9)
}
print(values)                             #{('int', 9), ('float', 9.0)}
print(len(values))                       #<class 'set'>





















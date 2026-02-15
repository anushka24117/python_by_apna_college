# dict={
#     "name":"Anushka",
#     "cgpa":9.6,
#     "marks":[98,97,96],
# }

# print(dict)
# print(dict["name"])
# print(dict["cgpa"])
# print(dict["marks"])


# info={
#     "key":"value",
#     "name":"apnacllg",
#     "learning":"coding",
#     "age":76,
#     "is_adult":True,
#     "marks":94.4,
# }

# print(info)

# info={
#     "name":"apnacllg",
#     "subjects":["python","c","java"],
#     "topics":("dict","set"),
#     "age":35,
#     "is_adult":True,
#     "marks":94.4,
# }
# print(type(info))
# print(info["name"])
# print(info["topics"])
# print(info["subjects"])
# print(info["age"])

# info={
#     "name":"apnacllg",
#     "subjects":["python","c","java"],
#     "topics":("dict","set"),
#     "age":35,
#     "is_adult":True,
#     "marks":94.4,
# }

# print(info["surname"]) #error
# info["name"]="Anushka"  #changed value from apnacllg to Anushka
# print(info)

# info={
#     "name":"apnacllg",
#     "subjects":["python","c","java"],
#     "topics":("dict","set"),
#     "age":35,
#     "is_adult":True,
#     "marks":94.4,
# }

# info["name"] = "Anushka"  #name value is changed
# info["surname"] = "Kumari"  #surname is added
# print(info)


#TO create null dict
# null_dict={}
# null_dict["name"]="apnacllg"
# print(null_dict)

#To print Nested Dictionary
# Student={
#     "name":"rahul Kumar",
#     "subjects":{
#         "phy":97,
#         "chem":98,
#         "math":95,
#     }
# }

# print(Student)
# print(Student["subjects"])
# print(Student["subjects"]["phy"])


# To print Dictionary_methods

# student={
#     "name":"rahul Kumar",
#     "subjects":{
#         "phy":97,
#         "chem":98,
#         "math":95,
#     }
# }

# print(student.keys())
# print(len(student))
# print(list(student.keys()))
# print(len(list(student.keys())))
# print(student.values())
# print(list(student.values()))
# print(student.items())
# print(list(student.items()))

# To print Dictionary_methods
# student={
#     "name":"rahul Kumar",
#     "subjects":{
#         "phy":97,
#         "chem":98,
#         "math":95,
#     }
# }

# pairs=list(student.items())
# print(pairs[0])


#d["key"]
#d.get("key")


# student={
#     "name":"rahul Kumar",
#     "subjects":{
#         "phy":97,
#         "chem":98,
#         "math":95,
#     }
# }

# print(student["name"])           #rahul kumar
# print(student.get("name"))       #rahul kuamr

# student={
#     "name":"rahul Kumar",
#     "subjects":{
#         "phy":97,
#         "chem":98,
#         "math":95,
#     }
# }
# print(student["name2"])



# student={
#     "name":"rahul Kumar",
#     "subjects":{
#         "phy":97,
#         "chem":98,
#         "math":95,
#     }
# }


# print(student.get("name2"))


# student={
#     "name":"rahul Kumar",
#     "subjects":{
#         "phy":97,
#         "chem":98,
#         "math":95,
#     }
# }

# print(student["name2"]) #error
# print("hyy")            #fails to execute due to error
# print("python")         #fails to execute due to error



# student={
#     "name":"rahul Kumar",
#     "subjects":{
#         "phy":97,
#         "chem":98,
#         "math":95,
#     }
# }

# student.update({"city":"delhi"})
# print(student)

# student={
#     "name":"rahul Kumar",
#     "subjects":{
#         "phy":97,
#         "chem":98,
#         "math":95,
#     }
# }

# new_dict={"city":"new delhi"}
# student.update(new_dict)
# print(student)


student={
    "name":"rahul Kumar",
    "subjects":{
        "phy":97,
        "chem":98,
        "math":95,
    }
}

new_dict={"name":"neha kumar","age":16}
student.update(new_dict)
print(student)
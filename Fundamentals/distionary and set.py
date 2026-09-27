#dictionary is the storage of number in  (key :value)
# info={
#     "key" : "value",
#     "name" : "ankush",
#     "age" : 45,
#     "subject" : [ "python", "c++", " java"],
#     "topic" : ("dict", "set")
# }
# # we can not write same key again
# print(info)
# print(info["name"])
# print(info["key"])

# info["name"] = "arsh tiwari"
# info["surname"] = "tripathi"
# print(info)


# # nested dictionary
# student = {
#     "name" : "arsh tiwari",
#     "subject" : {
#         "chemistry" : 89,
#         "maths" : 95,
#         "physics" : 94
#     }
# }
# print(student)
# print(student["subject"]["chemistry"])

# # mathod for dictionary
# student = {
#     "name" : "arsh tiwari",
#     "subject" : {
#         "chemistry" : 89,
#         "maths" : 95,
#         "physics" : 94
#     }
# }
# print(student)

# print(student.keys())
# print(student.values())
# print(student.items())
# print(student.get("name"))# this get mathod is importent becouse when key is not exist int he disctionary it will return none not error
# new_dict = {"city" : "mumbai",}
# print(student.update(new_dict))
# print(student) 



# # set in python
# # collaction of unordered numebr(element must be unique and immutable)
# #duplicate value are not allow in the set
# collaction = {1,5,2,4,2,1,6}
# print(collaction)
# print(type(collaction))
# print(len(collaction)) #total number of the item

# collaction = set()# for the emplty set
# # method
collaction = {1,5,2,4,2,1,6}
print(type(collaction))
print(collaction)

# collaction.add(25)
# print(collaction)

# collaction.remove(25)
# print(collaction)

# collaction.pop()
# print(collaction)

# collaction.clear()
# print(len(collaction))


# set1 = {1,2,3,4}
# set2 = {3,4,5,6}
# print(set1.union(set2))
# print(set1.intersection(set2))



# #Question number 1(store the word meaning in the python dictionary)

# word_meaning = {
#     "table" : ["a piece of forniture","list of fact and figure"],
#     "cat" : "a small animal"
# }
# print(word_meaning)
# print(type(word_meaning))

# #question number 2 (count the needed classroom for the student for each subject)
# subject = {"python","java","c++", "python","javascript","java", "python","java","c++","c"}
# print(subject)
# print(len(subject))



# #store number one by one in dictinary entered  by thr user
# subject = {}
# subject1 = {"meths" : int(input("enetr your maths mark :- "))}
# subject.update(subject1)
# print(subject)
# subject2 = {"chemistry" : int(input("enter your chemistry mark:- "))}
# subject.update(subject2)
# print(subject)
# subject3 = {"physics" : int(input("enter your physics mark :-"))}
# subject.update(subject3)
# print(subject)
# print()


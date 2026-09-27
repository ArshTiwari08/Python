# print("hello world")
# #  List(built in data type to store the value)
# marks = [4,5,26,25]
# print(marks[3])
# print(type(marks))
# print(len(marks))

# #  in python we can store  different datatype value
# #  Slicing is possible in the list

# print(marks[1:3])
# mark = [4,5,26,25]
# mark.append(78)
# print(mark)

# marks = [4,5,26,25]
# marks.sort()
# print(marks)

# marks = [4,5,26,25]
# marks.sort(reverse=True)
# print(marks)

# marks = [4,5,26,25]
# marks.reverse()
# print(marks )

# marks = [4,5,26,25]
# marks.insert(2,87)
# print(marks)

# marks = [4,5,26,25]
# marks.remove(5)# its remove the first occurence of the number
# print(marks)

# marks = [4,5,26,25]
# marks.pop(3)# its remove the number at the index  of the number
# print(marks)




# # TUPLE(store of immutable  datatype value)

# marks = (4,5,26,25)
# print(marks)
# print(type(marks))

# #   slicing same work as list

# # mathod
# marks = (4,5,26,25)
# print(marks.index(26))

# marks = (4,5,26,25)
# print(marks.count(26))


# # Question number 1 :
# movie = []

# a = movie.append(input("enter your  first movie name:-"))
# b = movie.append(input("enter your  second movie name:- "))
# c = movie.append(input("enter your  third movie name:- "))
# print(movie)


# # to check the number are pelendrom or not
# marks = [1,2,3,2,1]
# mark =  [ 2,7.9,29]
# a = mark.copy()
# a.reverse()
# if marks == a:
#     print("number are pelindrom")
# else:
#     print("number are not pelindrom")


# # other question are created by using the fuction




# def juggler_sequence(n):
#     sequence = [n]  # Start with the given number
#     while n != 1:
#         if n%2 == 0:
#             n = int(n**0.5)
#         else:
#             n = int(n**1.5)
#         sequence.append(n)
#     return sequence
# print(juggler_sequence(7))
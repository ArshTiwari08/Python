# f = open("demo.txt", "r")# r is default mode
# data = f.read()
# print(data)
# print(type(data))
# f.close()
# data = f.read()
# print(data)

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# f.close()


# Writting in file
# f = open("demo.txt", "w")
# f.write("aditya is brother of ankush tiwari.123 \n")
# f.write("indian is best cuntry for leaving ")
# f.close()

# f = open("demo.txt", "a+")
# f.write("ankush is student of computer science student")
# data = f.read()
# print(data)


#WITH SYNTEX
# with open("demo.txt","r") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt","w") as f:
#     f.write("new data")

# import os
# os.remove("demo.txt")

# with open("prcatice","w") as f:
#     f.write("hii everyone\nwe are learning file I/O\n")
#     f.write("using java.\ni like programming in java ")

# with open("prcatice","r") as f:
#     data = f.read()

# new_data = data.replace("java","python")
# print(new_data)

# with open("prcatice","w") as f:
#     f.write(new_data)
# def check_for_word():
#     word = "learning"
#     with open("prcatice","r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("found")
#         else:
#             print("not found")
# check_for_word()

# with open("practice.txt","w") as f:
#     f.write("hii everyone\nwe are learning file I/O\n")
#     f.write("using java.\ni like programming in java ")

# def check_for_line():
#     word = "learning"
#     data = True
#     line_no= 1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return-1
# check_for_line()

# count = 0
# with open("prcatice.txt","r") as f:
#     data = f.read()
#     print(data)

    # num = ""
    # for i in range(len(data)):
    #     if(data[i] == ","):
    #         print(num)
    #         num = ""
    #     else:
    #         num += data[i]

#     nums = data.split(",")
#     for val in nums:
#         if(int(val) % 2 == 0):
#             count += 1
# print(count)


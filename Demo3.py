val = [1, 2, "thom", 4.5]
print(val[1])
val[2] = "test"
print(val[2])

#dictionary {}
dic = {"a" : 2 , 4 : "abc", "c" : "Hello world"}
print("-------")
print(dic[4])
print(dic["c"])
print("-------")

dict ={}

dict["firstname"] = "Thom"
dict["lastname"] = "Nguyen"
dict["age"] = 33
print(dict)
#update
print("-------")
dict["age"] = 18.5
print(dict)
print("-------") # delete
del dict["age"]
print(dict)
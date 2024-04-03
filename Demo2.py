values = [1, 2, "thom", 4, 5]   #list

# print value 1
print(values[0])

print(values[4]) # 4
print(values[-1]) # 5 , vị trí cuối
print(values[1:3]) # 1, 2 - in ra value vi tri 1 va 2

values.insert(3, "tesst") # vi tri 3, chen vao text tesst
print(values)

values.append("End") # them "End" vao cuoi list
print(values)

values[2] = "Python"  #update date
print(values)

del values[0]    #delete data
print(values)
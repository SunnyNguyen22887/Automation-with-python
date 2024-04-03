str = "rahulshettyacademy.com"
str1 = "consulting firm"
str3 = "rahulshetty"

print(str[1]) # index from 0
print(str[0:5]) # if you want to get substring 0 -> j-1
print(str[-1]) # in ra value cuối
print(str+str1) #concatenation - ghép chuỗi

print(str3 in str) # in ra true/false - substring check (check xem có phải con k)
var = str.split(".")
print(var)
print(var[0])
str4 = "  great "
print(str4.strip()) # cắt khoảng trắng
print(str4.lstrip()) # cắt khoảng trắng bên trái
print(str4.rstrip()) # cắt khoảng trăng bên phải

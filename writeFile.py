# with open('test.txt','r') as reader: # w : open file with write mode, r is read mode
#     content = reader.readlines()
#     reversed(content) # đảo ngược các phần tử trong file
#     with open('test.txt','w') as writer:
#         for line in reversed(content):
#             writer.write(line)
# https://www.geeksforgeeks.org/writing-excel-sheet-using-python/
print("------------write excel file--------------")
import xlwt
from xlwt import Workbook

# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Data')
#(row-column)
sheet1.write(1, 0, 'ISBT DEHRADUN')
sheet1.write(2, 0, 'SHASTRADHARA')
sheet1.write(3, 0, 'CLEMEN TOWN')
sheet1.write(4, 0, 'RAJPUR ROAD')
sheet1.write(5, 0, 'CLOCK TOWER')
sheet1.write(0, 1, 'ISBT DEHRADUN')
sheet1.write(0, 2, 'SHASTRADHARA')
sheet1.write(0, 3, 'CLEMEN TOWN')
sheet1.write(0, 4, 'RAJPUR ROAD')
sheet1.write(0, 5, 'CLOCK TOWER')

wb.save('example.xlsx')
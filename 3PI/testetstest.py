import openpyxl

book = openpyxl.load_workbook("C:\\Users\\satheeshnair\\PycharmProjects\\3PI\\Testdata\\Testdata.xlsx")
sheet = book.active
rows = sheet.max_row
cols = sheet.max_column

for col in range(1,cols+1):
    for row in range(2,rows+1):
        testcasename = sheet.cell(row=row,column=col).value
        if (testcasename == "test_order"):
            methodname = sheet.cell(row=row,column=col+1).value
            if(methodname == "order"):
                value = sheet.cell(row=row,column=col+2).value
                print(value)


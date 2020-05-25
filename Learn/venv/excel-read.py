import openpyxl

path=r"C:\\Users\satheeshnair\PycharmProjects\Learn\venv\Testdata.xlsx"

workbook = openpyxl.load_workbook(path)

sheet = workbook.get_sheet_by_name("admin") #workbook.active

rows = sheet.max_row
cols = sheet.max_column

print(rows)
print(cols)

for r in range(1, rows+1):
    for c in range(1, cols):
        print(sheet.cell(row=r,column=c).value, end = '             ')

    print()


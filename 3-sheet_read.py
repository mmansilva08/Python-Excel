from openpyxl import load_workbook

#lê uma pasta de trabalho
wb = load_workbook("data/pivot_table.xlsx")

sheet = wb ["Relatório"]
#ACESSANDO UM VALOR ESPECIFICO
# print(sheet["A3"].value)
# print(sheet["B3"].value)

# 3 ITERANDO VALORES POR MEIO DE UM LOOP
for i in range(2, 6 ):
    ano = sheet["A%s" %i].value
    am = sheet["B%s" %i].value
    bt = sheet["C%s" %i].value
    print("{0} O Aston martin vendeu {1} e o bentley vendeu {2}".format(ano, am,bt))
   
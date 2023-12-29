import pandas as pd
#importando dados
data = pd.read_excel("data/VendaCarros.xlsx")
# print(type(data))

#selecionando colunas especificas do dataframe
df = data [["Fabricante", "ValorVenda","Ano"]]
print(df)

pivot_table = df.pivot_table(
    index="Ano",
    columns="Fabricante",
    values="ValorVenda",
    aggfunc="sum"
)
print(pivot_table)

#exportando tabela pivô em arquivo excel
pivot_table.to_excel("data/pivot_table.xlsx", "Relatório")


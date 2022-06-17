import pandas as pd

x = pd.read_excel(r"C:\Users\samueljo\Desktop\bh_bus\teste.xlsx")


filtro = x['TITULO1'] == 'teste1'


print(x[filtro])

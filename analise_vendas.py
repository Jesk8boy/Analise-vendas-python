import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

df = pd.read_csv("vendas.csv", parse_dates=["Data"])
df["Faturamento"] = df["Quantidade"] * df["Preco_Unitario"]
df["Mes"] = df["Data"].dt.to_period("M")

faturamento_mensal = df.groupby("Mes")["Faturamento"].sum()
produtos_vendidos = df.groupby("Produto")["Quantidade"].sum()
faturamento_regiao = df.groupby("Região")["Faturamento"].sum()

faturamento_mensal.plot(kind="bar", title="Faturamento Mensal", ylabel="R$")
plt.tight_layout()
plt.savefig("faturamento_mensal.png")
plt.clf()

produtos_vendidos.plot(kind="bar", title="Produtos Mais Vendidos", ylabel="Unidades")
plt.tight_layout()
plt.savefig("produtos_mais_vendidos.png")
plt.clf()

faturamento_regiao.plot(kind="pie", autopct='%1.1f%%', title="Faturamento por Região")
plt.ylabel("")
plt.tight_layout()
plt.savefig("faturamento_por_regiao.png")
plt.clf()

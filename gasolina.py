# código de geração do gráfico 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Importando os dados CSV, para um DataFrame 
data = pd.read_csv("gasolina.csv")

#Gerando um gráfico simples dos dias X preço

with sns.axes_style("darkgrid"):
  grafico = sns.lineplot(data=data, x="dia", y="venda")
  grafico.set(title="Preço do combustível VS 10 primeiros dias de Julho de 2021", xlabel="Dias de Julho de 2021", ylabel="Preço em Reais")
  grafico.set_xticks(data["dia"])
  grafico.set_xlim(1, data["dia"].max())
  
  #Salvando o Gráfico em um arquivo PNG
  plt.savefig("Preco_do_combustivel_VS_10_primeiros_dias_de_Julho_de_2021.png", dpi=350, bbox_inches="tight")

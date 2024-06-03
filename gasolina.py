import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Importando os dados CSV, para um DataFrame 
data = pd.read_csv("gasolina.csv")

#Gerando um gráfico simples dos dias X preço

with sns.axes_style("darkgrid"):
  grafico = sns.lineplot(data=data, x="dia", y="venda")
  grafico.set(title="Evolução do preço do combustível ao longo dos dias", xlabel="Dias", ylabel="Preço (R$)")
  grafico.set_xticks(data["dia"])
  grafico.set_xlim(1, data["dia"].max())
  
  #Salvando o Gráfico em um arquivo PNG
  plt.savefig("Grafico_dias_x_preco_gasolina_sp.png", dpi=350, bbox_inches="tight")

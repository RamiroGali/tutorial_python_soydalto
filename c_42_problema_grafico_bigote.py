import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar database en un dataFrame
df = pd.read_csv("src/db_categoria_valor.csv")

# Cargar el gráfico antes de visualizarlo en una nueva ventana
sns.boxplot(x="categoria", y="valor", data=df)

# Mostrar gráfico previamente cargado
plt.show()

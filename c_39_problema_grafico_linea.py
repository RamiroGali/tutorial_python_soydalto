import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar database en un dataFrame
df = pd.read_csv("src/db_date.csv")

# Cargar el gráfico antes de visualizarlo en una nueva ventana
sns.lineplot(x="fecha", y="cantidad", data=df)

# colocar un punto
plt.plot("01-09", 17, "o")

# Mostrar gráfico previamente cargado
plt.show()

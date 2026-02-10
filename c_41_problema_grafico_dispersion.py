import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar database en un dataFrame
df = pd.read_csv("src/db_tiempo_dinero.csv")

# Cargar el gráfico antes de visualizarlo en una nueva ventana
sns.scatterplot(x="tiempo", y="dinero", data=df)

# Mostrar gráfico previamente cargado
plt.show()

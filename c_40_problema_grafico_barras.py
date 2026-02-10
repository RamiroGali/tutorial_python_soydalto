import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar database en un dataFrame
df = pd.read_csv("src/db_ingresos.csv")

# Cargar el gráfico antes de visualizarlo en una nueva ventana
sns.barplot(x="fuente", y="ingresos", data=df)

total_ingresos = df["ingresos"].sum()

print(f"El total de ingresos es de: ${total_ingresos} USD")

# Mostrar gráfico previamente cargado
plt.show()

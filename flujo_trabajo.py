from scripts.procesamiento_datos import cargar_datos, obtener_tipos_variables, guardar_csv
from scripts.dividir_datos import dividir_datos
import os

# Rutas
ruta_datos = "data"
ruta_salida = "outputs/dataset_completo.csv"

# Cargar datos
df = cargar_datos(ruta_datos)

# Obtener tipos de variables
numericas, categoricas = obtener_tipos_variables(df)

# Guardar el DataFrame completo
guardar_csv(df, ruta_salida)

# Dividir los datos
X_train, X_test, y_train, y_test = dividir_datos(df, columna_objetivo="Class")

# Guardar conjuntos divididos
guardar_csv(X_train, "outputs/X_train.csv")
guardar_csv(X_test, "outputs/X_test.csv")
guardar_csv(y_train.to_frame(), "outputs/y_train.csv")
guardar_csv(y_test.to_frame(), "outputs/y_test.csv")
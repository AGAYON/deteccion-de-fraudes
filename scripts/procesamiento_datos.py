import pandas as pd
import os

def cargar_datos(ruta_datos):
    """
    Carga el dataset creditcard.csv desde la carpeta de datos.

    Parámetros:
        ruta_datos (str): Ruta a la carpeta que contiene el CSV.

    Retorna:
        pd.DataFrame: Dataset cargado.
    """
    ruta_archivo = os.path.join(ruta_datos, 'creditcard.csv')
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"No se encontró el archivo en la ruta: {ruta_archivo}")
    
    df = pd.read_csv(ruta_archivo)
    return df

def obtener_tipos_variables(df):
    """
    Separa nombres de columnas numéricas y categóricas.

    Parámetros:
        df (pd.DataFrame): DataFrame.

    Retorna:
        tuple: (numericas, categoricas).
    """
    numericas = df.select_dtypes(include=['number']).columns.tolist()
    categoricas = df.select_dtypes(include=['object', 'category']).columns.tolist()
    return numericas, categoricas

def guardar_csv(df, ruta_salida):
    """
    Guarda el DataFrame en formato CSV.

    Parámetros:
        df (pd.DataFrame): DataFrame a guardar.
        ruta_salida (str): Ruta completa al archivo destino.
    """
    df.to_csv(ruta_salida, index=False)

def resumen_df(df, max_unicos=5):
    """
    Muestra un resumen tipo 'glimpse' de cada columna del DataFrame.

    Parámetros:
        df (pd.DataFrame): El DataFrame a analizar.
        max_unicos (int): Número máximo de ejemplos únicos a mostrar por columna.

    Retorna:
        pd.DataFrame: Resumen con nombre, tipo, % de nulos, únicos y ejemplos.
    """
    resumen = []

    for col in df.columns:
        tipo = df[col].dtype
        nulos = df[col].isnull().mean() * 100
        unicos = df[col].nunique()
        ejemplo = df[col].dropna().unique()[:max_unicos]

        resumen.append({
            "columna": col,
            "tipo": tipo,
            "% nulos": round(nulos, 1),
            "valores únicos": unicos,
            "ejemplos": ejemplo
        })

    resumen_df = pd.DataFrame(resumen)
    return resumen_df
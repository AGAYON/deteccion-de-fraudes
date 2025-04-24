# scripts/preprocessing.py
import pandas as pd
import os




def load_data(data_dir):
    """
    Carga el dataset creditcard.csv desde la carpeta de datos.

    Parameters:
        data_dir (str): Ruta a la carpeta que contiene el CSV

    Returns:
        pd.DataFrame: Dataset cargado
    """
    file_path = os.path.join(data_dir, 'creditcard.csv')
    print("Cargando datos desde:", file_path)

    df = pd.read_csv(file_path)
    print(f"Dataset cargado con forma: {df.shape}")
    return df





def get_feature_types(df):
    """
    Separa nombres de columnas numéricas y categóricas.
    
    Parameters:
        df (pd.DataFrame): DataFrame
    
    Returns:
        tuple: (numericas, categoricas)
    """
    numericas = df.select_dtypes(include=['number']).columns.tolist()
    categoricas = df.select_dtypes(include=['object', 'category']).columns.tolist()

    print(f"Variables numéricas:   {len(numericas)}")
    print(f"Variables categóricas: {len(categoricas)}")

    return numericas, categoricas


def guardar_csv(df, output_path):
    """
    Guarda el DataFrame en formato CSV.
    
    Parameters:
        df (pd.DataFrame): DataFrame a guardar
        output_path (str): Ruta completa al archivo destino
    """
    df.to_csv(output_path, index=False)
    print(f"Archivo guardado en: {output_path}")


def glimpse_df(df, max_unique=5):
    """
    Muestra un resumen tipo 'glimpse' de cada columna del DataFrame.

    Parameters:
        df (pd.DataFrame): El DataFrame a analizar
        max_unique (int): Número máximo de ejemplos únicos a mostrar por columna

    Returns:
        pd.DataFrame: Resumen con nombre, tipo, % de nulos, únicos y ejemplos
    """
    resumen = []

    for col in df.columns:
        tipo = df[col].dtype
        nulos = df[col].isnull().mean() * 100
        unicos = df[col].nunique()
        ejemplo = df[col].dropna().unique()[:max_unique]

        resumen.append({
            "columna": col,
            "tipo": tipo,
            "% nulos": round(nulos, 1),
            "valores únicos": unicos,
            "ejemplos": ejemplo
        })

    resumen_df = pd.DataFrame(resumen)
    return resumen_df

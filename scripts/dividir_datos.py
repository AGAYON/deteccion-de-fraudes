from sklearn.model_selection import train_test_split

def dividir_datos(df, columna_objetivo, test_size=0.3, random_state=42):
    """
    Divide los datos en conjuntos de entrenamiento y prueba.

    Parámetros:
        df (pd.DataFrame): DataFrame completo.
        columna_objetivo (str): Nombre de la columna objetivo.
        test_size (float): Proporción del conjunto de prueba.
        random_state (int): Semilla para reproducibilidad.

    Retorna:
        tuple: (X_train, X_test, y_train, y_test).
    """
    X = df.drop(columns=columna_objetivo)
    y = df[columna_objetivo]
    return train_test_split(X, y, test_size=test_size, stratify=y, random_state=random_state)
from sklearn.metrics import precision_score, recall_score, f1_score
import numpy as np

def ajustar_umbral(y_true, y_prob, thresholds):
    """
    Ajusta el umbral de predicción y calcula métricas para cada umbral.

    Parámetros:
        y_true (array-like): Valores reales de la clase objetivo.
        y_prob (array-like): Probabilidades predichas por el modelo.
        thresholds (array-like): Lista de umbrales a evaluar.

    Retorna:
        list: Lista de tuplas con (umbral, precision, recall, F1-Score).
    """
    resultados = []
    for threshold in thresholds:
        y_pred_threshold = (y_prob >= threshold).astype(int)
        precision = precision_score(y_true, y_pred_threshold)
        recall = recall_score(y_true, y_pred_threshold)
        f1 = f1_score(y_true, y_pred_threshold)
        resultados.append((threshold, precision, recall, f1))
    return resultados
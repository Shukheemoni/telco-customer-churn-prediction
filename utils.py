import numpy as np
from sklearn.metrics import recall_score, f1_score


def evaluate_model(model, X_test, y_test):
    """
    Evaluate a trained model using Recall and F1-score.
    """
    y_pred = model.predict(X_test)

    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    return recall, f1


def get_scale_pos_weight(y):
    """
    Compute scale_pos_weight for imbalanced datasets (used in XGBoost).
    """
    neg, pos = np.bincount(y)
    return neg / pos

from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self, n_estimators=100, contamination=0.1):
        """Initialize the AnomalyDetector with the ISOLATION FOREST model."""
        self.model = IsolationForest(n_estimators=n_estimators, contamination=contamination)

    def fit(self, X):
        """Fit the model to the data."""
        self.model.fit(X)

    def predict(self, X):
        """Predict anomalies in the data."
        predictions = self.model.predict(X)
        # Convert the predictions to a more interpretable form: 1 for normal, -1 for anomaly
        return [1 if pred == 1 else -1 for pred in predictions]

    def fit_predict(self, X):
        """Fit the model and predict anomalies."""
        self.fit(X)
        return self.predict(X)


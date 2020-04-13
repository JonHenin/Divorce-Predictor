class PredictData():
    def __init__(self, model = None):
        self.model = model
        self.pred = []

    # Use model that is supplied when calling PredictData or use a different model if one is specified.
    def predict(self, X_test, model = None):
        if model != None:
            self.pred = model.predict_proba(X_test)
        else:
            self.pred = self.model.predict_proba(X_test)

        return self.pred

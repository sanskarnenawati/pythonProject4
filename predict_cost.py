import joblib


def predict(data):
    lr = joblib.load('rentpred.sav')
    return lr.predict(data)
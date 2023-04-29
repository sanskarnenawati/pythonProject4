import joblib


def predict(data):
    lr = joblib.load('rw.joblib')
    return lr.predict(data)

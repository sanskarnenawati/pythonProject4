import joblib


def predict(data):
    lr = joblib.load('rf.joblib')
    return lr.predict(data)

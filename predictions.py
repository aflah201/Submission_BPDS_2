import joblib

model = joblib.load('./model/gboost_model.joblib')
result_target1 = ['Dropout', 'Graduate/Enrolled']

def predictions(data):
    result = model.predict(data)
    return result_target1[result[0]]
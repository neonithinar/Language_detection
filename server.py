import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from tensorflow import keras
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


app = Flask(__name__)
with open('vectorizer.pkl', 'rb') as f:
    vectorizer_loaded = pickle.load(f)


def preprocess_input(text):
    data = text
    # data = pd.DataFrame(data)
    # df_predict = pd.DataFrame(data, columns=["text"])
    # df_predict["text"] = df_predict["text"].str.lower()
    # df_predict["text"] = df_predict['text'].str.replace(r'[^\w\s]+', '')
    data = data.lower()
    data = data.replace(r'[^\w\s]+', '')
    data = [data]

    X = vectorizer_loaded.fit_transform(data)
    feature_names = vectorizer_loaded.get_feature_names()
    predict_features = pd.DataFrame(data=X.toarray(), columns=feature_names)
    return predict_features


predicted_lang = ["arabic", "czech", "danish", "finnish", "lithuanian", "macedonian",
                  "dutch", "polish", "serbian", "swedish"]

# text = "Mogu li da vam (polite) / ti pomognem?" # some  sentence from any of the above language


# load the model
model_prep = keras.models.load_model("model_1.h5")

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict', methods= ['POST'])
def predict():
    # render the results from HTML GUI
    # Get the data from the POST request.
    data =str(request.form.values())
    data = data.lower()
    data = data.replace(r'[^\w\s]+', '')
    data = [data]

    X = vectorizer_loaded.fit_transform(data)
    feature_names = vectorizer_loaded.get_feature_names()
    X_pred = pd.DataFrame(data=X.toarray(), columns=feature_names)

    # if

    # Make prediction using model loaded from disk as per the data.
    var = np.argmax(model_prep.predict(X_pred), axis=-1).item()  # store the array of prediction into a variable

    return render_template('index.html', prediction_text = "The input language is {}".format(predicted_lang[var]))

if __name__ == '__main__':
    app.run(port=5000, debug = True)
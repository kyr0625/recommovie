from flask import Flask, request, jsonify
import joblib
import numpy as np
from konlpy.tag import Okt

app = Flask(__name__)


def tw_tokenizer(text):
    twitter = Okt()
    tokens_ko = twitter.morphs(text)
    return tokens_ko


# json REST Flask API
@app.route('/sentiment/predict', methods=['POST'])
def predict():
    model = joblib.load('../grid_cv.pkl')
    model = model.best_estimator_
    tfidf_model = joblib.load('../tfidf_vect.pkl')
    review_texts = np.array(request.json['review_texts'])
    tfidf = tfidf_model.transform(review_texts)
    result = model.predict(tfidf)
    return jsonify(result.tolist())


if __name__ == '__main__':
    app.run(port=8080)



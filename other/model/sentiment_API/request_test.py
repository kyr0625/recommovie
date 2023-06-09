import requests
import json
import pandas as pd
import numpy as np

url = 'http://localhost:8080/sentiment/predict'

seperated_review = pd.read_csv('../../data/split0.csv', encoding='utf-8')
df = seperated_review.iloc[:200]
texts = df["document"].tolist()
label = df["label"].tolist()

data = {'review_texts': texts}
headers = {'Content-type': 'application/json'}
response = requests.post(url, data=json.dumps(data), headers=headers)

result = response.json()
print(result)
print(label)
print('Accuracy: ', np.mean(np.array(result) == np.array(label)))

print(response.json())



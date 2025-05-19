import json
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

class SentimentModel:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()
        self.train_data = [
            ("This product is amazing and very useful", "Positive"),
            ("Had a terrible experience", "Negative"),
            ("The product is nice and high quality", "Positive"),
            ("Terrible service, very dissatisfied", "Negative")
        ]
        self._train()

    def _train(self):
        texts, labels = zip(*self.train_data)
        X = self.vectorizer.fit_transform(texts)
        self.model.fit(X, labels)

    def predict(self, text):
        X = self.vectorizer.transform([text])
        label = self.model.predict(X)[0]
        score = max(self.model.predict_proba(X)[0])
        return label, score

    def update_model(self, text, label):
        self.train_data.append((text, label))
        self._train()

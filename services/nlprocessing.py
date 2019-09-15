from sklearn.feature_extraction.text import CountVectorizer
import json


class NLProcessing:

    def process_texts(self, texts: dict, n: int):

        texts_list = list(texts.values())
        keys = texts.keys()
        vectorizer = CountVectorizer(ngram_range=(n, n))
        X = vectorizer.fit_transform(texts_list)
        word_matrix = X.toarray()
        processed_texts = {'word_vector_' + key: value.tolist() for key, value in zip(keys, word_matrix)}
        processed_texts["vocabulary"] = vectorizer.get_feature_names()

        return json.dumps(processed_texts)

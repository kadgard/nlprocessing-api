from sklearn.feature_extraction.text import CountVectorizer
import nltk
import json


class NLProcessing:


    def get_stopwords(self, language):
        if language:
            nltk.download('stopwords')
            return nltk.corpus.stopwords.words(language)
        else:
            return []


    def process_texts(self, texts: dict, n: int, language):
        stop_words = self.get_stopwords(language)
        texts_list = list(texts.values())
        keys = texts.keys()
        vectorizer = CountVectorizer(ngram_range=(n, n), stop_words=stop_words, strip_accents='ascii')
        X = vectorizer.fit_transform(texts_list)
        word_matrix = X.toarray()
        processed_texts = {'word_vector_' + key: value.tolist() for key, value in zip(keys, word_matrix)}
        processed_texts["vocabulary"] = vectorizer.get_feature_names()

        return json.dumps(processed_texts)

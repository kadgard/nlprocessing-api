## nlprocessing-api
This is a simple api to process texts, process them and return the vocabulary and word vectors.

#We will use the flask framework to comunication
http://flask.palletsprojects.com/en/1.1.x/

#To process the texts wi choose to apply de sklearn feature extraction methods from CountVectorizer
https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html

##Routes
The main route from our api is (/gram/n/texts). The parameter n represents the gram dimension.
A POST in this route will result in sending a json with texts in the contect and receiving de resulted vocabulary
and the given word vectors for each text. Te return will also be in a json format.


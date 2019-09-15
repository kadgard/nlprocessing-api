# nlprocessing-api
This is a simple api to process texts,it returns the vocabulary and word vectors.

We will use the flask framework to comunication
http://flask.palletsprojects.com/en/1.1.x/

To process the texts we choose to apply de sklearn feature extraction methods from CountVectorizer
https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html

NLTK - Natural Language Toolkit will be used to get list of stop words for different languages

## Routes
- The main route from our api is (/gram/n/texts). The parameter n represents the gram dimension.
A POST in this route will result in sending a json with texts in the contect and receiving de resulted vocabulary
and the given word vectors for each text. Te return will also be in a json format.

- If you pass a language parameter as query string the service will filter the vocabulary using the nltk stopwords list,
removing words that may not be important.

- No autentication is required in v1.

# Examples

I am runing my aplication localy exposing it in port 5000 as you can see in flask documentation or in my dockerfile

## 1)
Sending a request to http://127.0.0.1:5000/gram/1/texts

With body = {
	"texto1": "Vem vamos embora que espear não é saber",
	"texto2": "Quem sabe faz a hora nao espera contecer"
}

will result in {"word_vector_testo1": [0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1], "word_vector_texto2": [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0,
0, 0], "vocabulary": ["contecer", "embora", "espera", "esppear", "faz", "hora", "nao", "que", "quem", "sabe", "saber",
"vamos", "vem"]}

## 2)

Adding the language filter passing portuguese as parameter you can see that some words are ignored.

POST http://127.0.0.1:5000/gram/1/texts?language=portuguese

body = {
	"testo1": "Vem vamos embora que esppear não é saber",
	"texto2": "Quem sabe faz a hora nao espera contecer"
}
 Result: {"word_vector_testo1": [0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1], "word_vector_texto2": [1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
"vocabulary": ["contecer", "embora", "espera", "esppear", "faz", "hora", "nao", "sabe", "saber", "vamos", "vem"]}

Any languages covered by nltk can be used, if the language doesn't exist it will only be ignored

## 3)

Any attribute in the json file that is not a string will also be ignored. As you can see next

POST http://127.0.0.1:5000/gram/1/texts?language=portuguese

Body = {
	"testo1": "Vem vamos embora que esppear não é saber",
	"texto2": "Quem sabe faz a hora nao espera contecer",
	"notatext": 1
}

Will have the same result as example 2.

## 4)

You can change the parameter that defines the gram space by changing the url

POST http://127.0.0.1:5000/gram/2/texts?language=portuguese

Body = {
	"testo1": "Vem vamos embora que esppear não é saber",
	"texto2": "Quem sabe faz a hora nao espera contecer",
	"notatext": 1
}

Will result in {"word_vector_testo1": [1, 0, 1, 0, 0, 0, 1, 0, 1, 1], "word_vector_texto2": [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
"vocabulary": ["embora esppear", "espera contecer", "esppear nao", "faz hora", "hora nao", "nao espera", "nao saber",
"sabe faz", "vamos embora", "vem vamos"]}

## 5)
 You can send as much text as you can fit in the request memory
 
 POST http://127.0.0.1:5000/gram/1/texts

 body = {
	"texto": "O que é que a baiana tem",
	"texto2": "vatapa tem",
	"maistexto": "Mussum Ipsum, cacilds vidis litro abertis. Todo mundo vê os porris que eu tomo, mas ninguém vê os tombis que eu levo! Praesent malesuada urna nisi, quis volutpat erat hendrerit non. Nam vulputate dapibus. Nullam volutpat risus nec leo commodo, ut interdum diam laoreet. Sed non consequat odio. Copo furadis é disculpa de bebadis, arcu quam euismod magna.",
	"essenao": 100,
	"nemesse": ["Bulbasaur Lorem ipsum dolor sit amet, Squirtle consectetur adipiscing elit. Ivysaur Lorem ipsum dolor sit amet, consectetur adipiscing elit. Venusaur Lorem ipsum dolor sit amet, consectetur adipiscing elit. Charmander Lorem ipsum dolor sit amet, consectetur adipiscing elit. Charmeleon Lorem ipsum dolor sit amet, consectetur adipiscing elit. Charizard Lorem ipsum dolor sit amet, consectetur adipiscing elit."],
	"ultimoprometo": "Silvio Santos Ipsum um, dois três, quatro, PIM, entendeuam? Eu não queria perguntar isso publicamente, ma vou perguntar. Carla, você tem o ensino fundamentauam? É com você Lombardiam. Ma o Silvio Santos Ipsum é muitoam interesanteam. Com ele ma você vai gerar textuans ha haae. É namoro ou amizadeemm? Qual é a musicamm? Mah roda a roduamm. Ma! Ao adquirir o carnê do Baú, você estará concorrendo a um prêmio de cem mil reaisam. Ma vai pra lá.",
	"mentira": "vai vai vai"
    }

  The answer will be = {"word_vector_texto": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "word_vector_texto2":
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], "word_vector_maistexto": [1, 0, 0, 0, 1, 0, 0,
1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 2, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0,
1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 2, 1, 1, 2, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 2, 0, 1, 0, 1, 0, 0, 0, 1, 0,
0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 2, 1, 0, 2, 0, 1], "word_vector_ultimoprometo": [0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 2,
0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 1, 5, 0, 1, 0, 0, 1, 1,
0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 2, 0, 2, 1, 1, 0, 0, 0, 1,
2, 0, 0, 2, 0, 0, 0, 4, 0, 1, 0], "word_vector_mentira": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0,
0, 0, 0], "vocabulary": ["abertis", "adquirir", "amizadeemm", "ao", "arcu", "baiana", "bau", "bebadis", "cacilds",
"carla", "carne", "cem", "com", "commodo", "concorrendo", "consequat", "copo", "dapibus", "de", "diam", "disculpa",
"do", "dois", "ele", "ensino", "entendeuam", "erat", "estara", "eu", "euismod", "fundamentauam", "furadis", "gerar",
"ha", "haae", "hendrerit", "interdum", "interesanteam", "ipsum", "isso", "la", "laoreet", "leo", "levo", "litro",
"lombardiam", "ma", "magna", "mah", "malesuada", "mas", "mil", "muitoam", "mundo", "musicamm", "mussum", "nam",
"namoro", "nao", "nec", "ninguem", "nisi", "non", "nullam", "odio", "os", "ou", "perguntar", "pim", "porris", "pra",
"praesent", "premio", "publicamente", "qual", "quam", "quatro", "que", "queria", "quis", "reaisam", "risus", "roda",
"roduamm", "santos", "sed", "silvio", "tem", "textuans", "todo", "tombis", "tomo", "tres", "um", "urna", "ut", "vai",
"vatapa", "ve", "vidis", "voce", "volutpat", "vou", "vulputate"]}


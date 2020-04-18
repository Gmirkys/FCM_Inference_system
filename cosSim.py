import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
stopwords = stopwords.words('english')

def clean_string(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    text = remove_Stopwords(text)
    return text

def remove_Stopwords(sentence):
    for word in stopwords:
        sentence = sentence.replace(word, '') 
    return sentence

def vectorize(quest):
    vectorizer = CountVectorizer().fit_transform(list(quest.values()))
    vectors = vectorizer.toarray()
    return vectors

def cosine_sim_vectors(vect1, vect2):
    vect1 = vect1.reshape(1, -1)
    vect2 = vect2.reshape(1, -1)
    return cosine_similarity(vect1, vect2)[0][0]

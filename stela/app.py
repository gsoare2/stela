import nltk 
from nltk.stem import RSLPStemmer

nltk.download('stopwords')

sentence = "A chave está na caixa azul"

def tokenize(sentence):
  sentence = sentence.lower()
  sentence = nltk.word_tokenize(sentence)
  return sentence

def stemming(sentence):
  stemmer = RSLPStemmer()
  phrase = []
  for word in sentence:
    phrase.append(stemmer.stem(word.lower()))
  return phrase

def remove_stop_words(sentence):
  stopwords = nltk.corpus.stopwords.words('portuguese')
  phrase = []
  for word in sentence:
    if word not in stopwords:
      phrase.append(word)
  return phrase

def train():
  training_data = []
  training_data.append({"class": "amor", "phrase": "Eu te amo"})
  training_data.append({"class": "amor", "phrase": "Eu gosto de você"})
  training_data.append({"class": "amor", "phrase": "Você é o amor da minha vida"})
  training_data.append({"class": "medo", "phrase": "estou com medo"})
  training_data.append({"class": "medo", "phrase": "tenho medo de fantasma"})
  training_data.append({"class": "localizacao", "phrase": "a marmita está na mesa"})
  training_data.append({"class": "localizacao", "phrase": "a bola está na sala"})
  print("%s frases incluidas" % len(training_data))
  return training_data

def learning(training_data):
  corpus_words = {}
  for data in training_data:
    frase = data['phrase']
    frase = tokenize(frase)
    frase = stemming(frase)
    frase = remove_stop_words(frase)
    class_name = data['class']
    if class_name not in list(corpus_words.keys()):
      corpus_words[class_name] = {}
    for word in frase:
      if word not in list(corpus_words[class_name].keys()):
        corpus_words[class_name][word] = 1
      else:
        corpus_words[class_name][word] += 1
  return corpus_words

data = train()
data = learning(data)

def calculate_class_score(sentence,class_name):
  score = 0 
  sentence = tokenize(sentence)
  sentence = stemming(sentence)
  for word in sentence:
    if word in data[class_name]:
      score += data[class_name][word]
  return score

def calculate_score(sentence):
  high_score = 0
  classname = 'default'
  for classe in data.keys():
    pontos = 0
    pontos = calculate_class_score(sentence,classe)
    if pontos > high_score:
      high_score = pontos
      classname = classe
  return classname, high_score

print(calculate_score("meu tênis está no meu quarto"))
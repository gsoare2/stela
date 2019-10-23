import nltk 
import re
import yaml
from nltk.stem import RSLPStemmer

expression = '[!-@[-`{-¿ÆÐÑ×ØÝ-ßä-æëðñö-øý-ÿ]'
stemmer = RSLPStemmer()


#Carrega o Corpus Words
def LoadMemory():
  fileW = open("words.nlp", 'r')
  words = fileW.read()
  words = yaml.load(words)
  return words

#Função responsavel por calcular a pontuação por classe
def calculate_class_score(sentence,class_name):
  score = 0
  sentence = re.sub(expression, '', sentence)
  sentence = nltk.word_tokenize(sentence)
  for word in sentence:
    if stemmer.stem(word.lower()) in corpus_words[class_name]:
      score += corpus_words[class_name][stemmer.stem(word.lower())]
  return score

#Função responsavel por classificar a frase
def classifique(sentence):
  high_class = None
  high_score = 0
  for c in list(corpus_words.keys()):
    score = calculate_class_score(sentence, c)
    if score > high_score:
      high_class = c
      high_score = score

  print(str(high_class))
  return high_class

memory = LoadMemory()
corpus_words = memory

# https://www.linkedin.com/pulse/classificação-de-textos-em-python-luiz-felipe-araujo-nunes
# https://www.kaggle.com/leandrodoze/examples-from-nltk-book-in-portuguese
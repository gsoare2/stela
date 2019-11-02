from nltk import tokenize, tag, chunk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

db = []
store_tokens = ['lembrar', 'registrar', 'guardar', 'armazenar', 'memorizar', 'recordar', 'relembrar', 'decorar', 'fixar', 'gravar', 'arquivar', 'salvar']
verb_list = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

def lemmatize_sentence(sentence):
  return " ".join([lemmatizer.lemmatize(w) for w in sentence.split()])

def tokenize_sentence(sentence):
  tokenized_sentence = tokenize.word_tokenize(sentence)
  return tag.pos_tag(tokenized_sentence)

def get_verb(sentence):
  for i in sentence:
    print(i[0], i[1])
    if (i[1] in verb_list and i[0] in store_tokens):
      return i[0]
  return None

def separate_verb(sentence, untokenized_sentence):
  action = get_verb(sentence)

  store(action, untokenized_sentence)

def store(action, completed_sentence):
  db.append({ action, completed_sentence })

def get_all():
  return db
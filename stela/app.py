import spacy
from utils.functions import cleanPhrase

nlp = spacy.load('pt')

message = 'a chave está na caixa azul'
clear_phrase = cleanPhrase(message)

parsed_message = nlp(clear_phrase)

for token in parsed_message:
  print(token.text, token.dep_)
  
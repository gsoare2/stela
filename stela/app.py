import nltk
from utils.functions import tokenize_sentence, separate_verb, get_all, lemmatize_sentence

# sentence = "me lembre que eu tenho uma entrevista hoje"

sentence = "amanhã tenho exame médico, pode me lembrar disso por favor?"
# sentence = "tomorrow I have and exam, can you remember me that please?"

# lemmatizated_sentence = lemmatize_sentence(sentence)
# print(lemmatizated_sentence)
tagged_sentence = tokenize_sentence(lemmatizated_sentence)
separate_verb(tagged_sentence, sentence)

for i in get_all():
  print(i)
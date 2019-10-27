import spacy
from utils.functions import normalize_sentence, get_all

nlp = spacy.load("pt")

sentence = 'me lembre que o nome do meu neto é joão'
message = nlp(sentence)
normalize_sentence(message, sentence)
print(get_all())
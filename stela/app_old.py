import spacy
from utils.functions import normalize_sentence, get_all, lemmatizate_sentence

nlp = spacy.load("pt")

original_sentence = 'me recorde que tenho uma entrevista hoje a noite'
tokenizated_sentence = nlp(original_sentence)
lematizated_sentence = lemmatizate_sentence(tokenizated_sentence)

processed_sentence = nlp(lematizated_sentence)

print(processed_sentence)

normalize_sentence(processed_sentence, original_sentence)
print(get_all())
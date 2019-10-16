import spacy

classification_tags = {
  'reminder': ['lembrar', 'recordar', 'memorizar', 'memorar']
}

nlp = spacy.load('pt')

print('Start conversation.\n')
message = input()

tokenized_message = nlp(message)

for token in tokenized_message:
  print(token.orth_, token.pos_, token.ent_type_)
      
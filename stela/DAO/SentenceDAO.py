def get_memory():
  fileW = open("words.nlp", 'r')
  words = fileW.read()
  fileW.close()
  words = yaml.load(words)
  return words

#Salva a corpus words
def save_memory(w):
  fileW = open("words.nlp", 'w')
  fileW.write(str(w))
  fileW.close()

#Carrega as frases que foram treinadas
def get_examples():
  fileE = open("examples.nlp", 'r')
  examples = fileE.read()
  fileE.close()
  return examples

#Salva as novas frases treinadas
def save_examples(example):
  fileE = open("examples.nlp", 'a')
  fileE.write(example + "\n")
  fileE.close()
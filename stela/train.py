import nltk 
import re
import yaml
from nltk.stem import RSLPStemmer

stemmer = RSLPStemmer()
expression = '[!-@[-`{-¿ÆÐÑ×ØÝ-ßä-æëðñö-øý-ÿ]'

#Carrega o Corpus Words
def LoadMemory():
    fileW = open("words.nlp", 'r')
    words = fileW.read()
    fileW.close()
    words = yaml.load(words)
    return words

#Carrega as frases que foram treinadas
def LoadExamples():
    fileE = open("examples.nlp", 'r')
    examples = fileE.read()
    fileE.close()
    return examples

#Salva a corpus words
def SaveMemory(w):
    fileW = open("words.nlp", 'w')
    fileW.write(str(w))
    fileW.close()

#Salva as novas frases treinadas
def SaveExample(example):
    fileE = open("examples.nlp", 'a')
    fileE.write(example + "\n")
    fileE.close()

#Massa de dados para exemplo
def Examples():
    training_data = []
    training_data.append({"class":"saudade", "sentence":"sinto sua falta"})
    training_data.append({"class":"saudade", "sentence":"estou com saudades"})

    training_data.append({"class":"fome", "sentence":"estou com fome"})
    training_data.append({"class":"fome", "sentence":"to faminto"})

    training_data.append({"class":"medo", "sentence":"to com medo"})
    training_data.append({"class":"medo", "sentence":"tomei um susto"})

    Learning(training_data)

#Função responsavel por treinar a frase
def Learning(training_data):
    corpus_words = LoadMemory()

    for data in training_data:
        examples = LoadExamples()
        sentence = data['sentence']
        sentence = re.sub(expression, '', sentence)
        sentence = stemmer.stem(sentence.lower())


        if sentence in examples:
            continue
        
        SaveExample(sentence)
        sentence = nltk.word_tokenize(sentence)
        class_name = data['class']
        if class_name not in list(corpus_words.keys()):
            corpus_words[class_name] = {}
        for word in sentence:
            if word not in list(corpus_words[class_name].keys()):
                corpus_words[class_name][word] = 1
            else:
                corpus_words[class_name][word] += 1

    
    SaveMemory(corpus_words)
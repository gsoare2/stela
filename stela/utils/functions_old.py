store_tokens = ['lembrar', 'registrar', 'guardar', 'armazenar', 'memorizar', 'recordar', 'relembrar', 'decorar', 'fixar', 'gravar', 'arquivar', 'salvar']
ignore_words = ['o', 'do', 'da', 'de', 'e', 'a', 'me', 'na', 'em', ' ', 'que', 'é', 'meu']
recover_tokens = ['onde', 'qual', 'quando', 'quem', 'oque', 'porque']
db = []

def lemmatizate_sentence(sentence):
  _word_list = []
  for _word in sentence:
    _word_list.append(_word.lemma_)
  return " ".join(_word_list)


def clean_phrase(phrase):
  _phrase = phrase.split()
  _remove_words = []
  for _t in _phrase:
    if _t in ignore_words:
      _remove_words.append(_t)
  [_phrase.remove(_s) for _s in _remove_words]
  return " ".join(_phrase)

def normalize_sentence(sentence, sentence_untokenized):
  action, index = find_root_verb(sentence, sentence_untokenized)
  predicate = find_predicate(sentence_untokenized, (index + len(action)))
  completed_phrase = sentence_untokenized

  store(action, predicate, completed_phrase, "10/10/10")

def find_root_verb(sentence, sentence_untokenized):
  for _word in sentence:
    if _word.pos_ == "VERB" and _word.dep_ == "ROOT" and _word.lemma_ in store_tokens:
      return _word, sentence_untokenized.index(_word.lemma_)

def find_predicate(sentence_untokenized, index):
  pattern_slice = slice(index, len(sentence_untokenized), 1)
  predicate = sentence_untokenized[pattern_slice]
  predicate = clean_phrase(predicate.lower())
  return predicate

def store(action, predicate, completed_phrase, date):
  db.append({"action": action, "predicate": predicate, "completed_phrase": completed_phrase, "date": date})

def get_all():
  return db
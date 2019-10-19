ignore_words = ['a', 'e', 'na']

def cleanPhrase(phrase):
  _phrase = phrase.split()
  for _t in _phrase:
    if _t in ignore_words:
      _phrase.remove(_t)
  return " ".join(_phrase)
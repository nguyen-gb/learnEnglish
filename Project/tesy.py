import random
from english_dictionary.scripts.read_pickle import get_dict
from googletrans import Translator


english_dict = get_dict()
wordDict = dict()

for i in range(4):
  x = random.choice(list(english_dict.items()))
  wordDict[x[0]] = x[1]

tmp = random.choice(list(wordDict.values()))
x = tmp.split(":")
x.remove('')

english_dict = get_dict()
wordDict = dict()
listWord = list()

for i in range(5):
  x = random.choice(list(english_dict.items()))
  wordDict["en"] = x[0]
  translator= Translator()
  wordDict["vn"] = translator.translate(x[1],  dest='vi').text
  listWord.append(wordDict)
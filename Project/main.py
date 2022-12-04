from flask import Flask, render_template, url_for, session, request
import random
from english_dictionary.scripts.read_pickle import get_dict
from collections.abc import MutableMapping
from googletrans import Translator
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def getVocab():
  english_dict = get_dict()
  wordDict = dict()

  for i in range(4):
    x = random.choice(list(english_dict.items()))
    wordDict[x[0]] = x[1]
  return wordDict

@app.route("/gameVocab")
def hello():
  result = getVocab()
  translator= Translator()
  rdVocab = random.choice(list(result.values()))
  if ":" in rdVocab: 
    tmp = rdVocab.split(":")
    tmp.remove('')
  else:
    tmp = rdVocab.split(":")
  
  temp = translator.translate(tmp[0],  dest='vi').text
  return render_template("index.html", result = result, randomVocab = temp, answer=rdVocab)

@app.route("/flashCard")
def flashCart():
  english_dict = get_dict()
  result = dict()
  translator= Translator()

  listWord = session.get('listWord')
  currWord = session.get('currnetWord')
  if listWord == None:
    listWord = list()
    currWord = int()
  
  args = request.args
  currentWord = int(args.get('currentWord'))
  action = int(args.get('action'))

  if action == 0:
    listWord = list(random.choices(list(english_dict.items()), k=100))
    result = listWord[0]
    currWord = 0
  else:
    result = listWord[currentWord]
    currWord = currentWord

  session["listWord"] = listWord
  session["currWord"] = currWord
  
  tmp = list(result)
  tmp[1] = translator.translate(result[1],  dest='vi').text
  result = tuple(tmp)
  return render_template("flashcards.html", result = result, currWord=currWord) 
  
if __name__ == "__main__":
  app.run(debug=True)
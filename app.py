from flask import Flask, render_template, url_for, request
import datetime

#
# ML Start
#

from difflib import get_close_matches
import json        
import spacy
import pandas as pd

stop_words=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", 
            "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", 
            "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", 
            "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", 
            "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", 
            "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", 
            "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", 
            "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", 
            "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
            "too", "very", "s", "t", "can", "will", "just", "don", "should", "now","%","people","sister","aaa","lot",
            "owls","love","wife","mom","son","friend","thanks","nails","daughter","name","friends"]

"""Load the pre-trained NLP model in spacy"""
import en_core_web_sm

nlp=spacy.load("en_core_web_sm") 
nlp.max_length=141690237

"""Define a function to extract keywords"""
def get_aspects(x):
    doc=nlp(x) ## Tokenize and extract grammatical components
    doc=[i.text for i in doc if i.text not in stop_words and i.pos_=="NOUN"] ## Remove common words and retain only nouns
    doc=list(map(lambda i: i.lower(),doc)) ## Normalize text to lower case
    doc=pd.Series(doc)
    doc=doc.value_counts().index.tolist()[:15] ## Get 15 most frequent nouns
    return doc

def predict(x):
  tags=get_aspects(x)
  l = []
  a = tags
  for i in range(len(a)):
      word = a[i]
      if word not in l:  
          x = get_close_matches(word, list(set(a)-set([word])), cutoff=0.75, n=1)
          if(len(x)>0):
              l.append(x[0])
  a = list(set(a)-set(l))
  return a

#
# ML END
#


app = Flask(__name__)
comments = []
string=''
for comment in comments:
    string=string+' '+(comment["comment"])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ledger')
def ledger():
    return render_template('Ledger.html')

@app.route('/Feedbacks', methods=['POST','GET'])
def feedback():
    if request.method == 'POST':
        date = datetime.date.today()
        data={
            "name": request.form['name'],
            "comment": request.form['comment'],
            "date": date
            }
        comments.append(data)
        global string
        string=string+' '+request.form['comment']
        keywords=predict(string)
        return render_template('Feedbacks.html', comments=comments, keywords=keywords)
    else:
        keywords=predict(string)
        return render_template('Feedbacks.html', comments=comments, keywords=keywords)

if(__name__ == "__main__"):
    app.run(debug=True)
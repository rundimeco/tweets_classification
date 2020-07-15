import re
from sklearn.feature_extraction import DictVectorizer
import json

class Struct:
  def __init__(self, **entries):
    self.__dict__.update(entries)

def load_json(path):
  f = open(path)
  data = json.load(f)
  f.close()
  return data

#TODO: vectorizer sklearn
def get_desc(chaine, options, dic_desc, test = True):
  m, M = [int(x) for x in re.split(",", options.len)]
  occs = {}
  for deb in range(len(chaine)):
    for i in range(m, M+1):
      desc = chaine[deb:deb+i]
      if test==True:
        if desc not in dic_desc:
          continue
      else:
        dic_desc.setdefault(desc, len(dic_desc))
      occs.setdefault(dic_desc[desc], 0)
      if options.freq==False:
        occs[dic_desc[desc]]+=1
      else:
        occs[dic_desc[desc]]+=1/float(len(chaine))
  return occs, dic_desc

def vectorize_tweets(tweets, model_name):
  desc = load_json(f"{model_name}.desc")
  options = Struct(**load_json(f"{model_name}.options"))
  X = []
  for tweet in tweets:
    occs, _ = get_desc(tweet, options, desc)
    X.append(occs)
  for num_desc in desc.values():
    if num_desc not in X[0]:
      X[0][num_desc] = 0
  dictvectorizer = DictVectorizer()
  X = dictvectorizer.fit_transform(X)
  return X

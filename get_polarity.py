from tools_classif import vectorize_tweets
from joblib import load

def tweet_polarity(tweets, model_name = "model/model_rbf"):
  if type(tweets) is str:
    tweets = [tweets]

  clf = load(f"{model_name}.joblib")
  X = vectorize_tweets(tweets, model_name) 
  return clf.predict(X)


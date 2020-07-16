**PURPOSE**

Classifying tweets (in French) with respect to polarity
Inspired by one of the machine learning model at character level used by Buscaldi et al. (http://people.irisa.fr/Cedric.Maigrot/CORIA-TALN-2018/Actes_TALN2018_vol2.pdf)

**INSTALLATION**

Some ML packages are needed, usually installing sklearn does the job. Another option if you have pip installed is to run the following command :

pip install -r requirements.txt

**RUNNING**

Run test.py to see if it works

the tweet_polarity function can take a single tweet (as a character string) or a list of tweets. The former solution is the best one if you have numerous tweets since loading the ML model is rather costlly.

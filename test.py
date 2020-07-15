from get_polarity import tweet_polarity

tests=[
       "Trop le seum",
       "C'est vraiment cool, je suis content",
       "Trop triste triste",
       "C'est heureux pour vous"
]

print(tweet_polarity(tests, model))

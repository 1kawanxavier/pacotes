from textblob import TextBlob

sentence = 'esse filme é otimo muito top gostei!'
blob = TextBlob(sentence)
sentiment = blob.sentiment.polarity
if sentiment > 0:
    print('Positivo')
elif sentiment < 0:
    print('Negativo')
else:
    print('Parcial')

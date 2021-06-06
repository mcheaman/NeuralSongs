import nltk
from nltk import ngrams

bi_train = []
with open("rockUnigrams.txt", "r") as file:
  text = file.read()
  for line in file:
    line = line.strip('\n')
    bi_train.append("<s> " + line + " </s>")

unigrams = nltk.word_tokenize(text)
bigram = list(nltk.bigrams(unigrams))
fdist1 = nltk.FreqDist(unigrams)
fdist2 = nltk.FreqDist(bigrams)
bi_prob = {}
bi_freq = []
preWord = token[0]
result = 0

for word in fdist1.most_common(len(10)):
    print(word, fdist1[word])

for word in len(fdist2):
  bigram = preWord + " " + token[word]
  for i in range(len(corpus_token) - 1):
    if (corpus_token[i] == preWord and corpus_token[i+1] == token[word]):
      result += 1
  bi_prob[fdist2] = result
  preWord = token[word]
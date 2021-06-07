from sys import argv
import nltk
from nltk import ngrams
from nltk import probability
from nltk.util import bigrams
import random
import math
# nltk.download()
bi_train = []
MAX_LINE_LEN = 8


with open("rockUnigrams.txt", "r") as file:
  for line in file:
    line = line.strip('\n')
    bi_train.append("<s> " + line + " </s>")
with open("rockUnigrams.txt", "r") as file:
  text = file.read()

unigrams = nltk.word_tokenize(text)
bigram = list(nltk.bigrams(unigrams))
fdist1 = nltk.FreqDist(unigrams)
fdist2 = nltk.FreqDist(bigram)
bi_prob = {}
bi_freq = []
result = 0

# for word in fdist1.most_common(10):
#     print(word)
# for word in fdist2.most_common(10):
#     print(word)

for word in fdist2.most_common(len(bigram)):
  bigram = word[0]
  bigram_frequency = word[1]
  unigram_frequncy = fdist1.get(bigram[0])
  probability = bigram_frequency/unigram_frequncy
  bi_prob[bigram] = probability


# count = 0
# for k,v in bi_prob.items():
#   print(f'{k}  ----> {v}')
#   count+=1
#   if(count == 10):
#     break;

bigram_sentences = []
bi_probability = []


def bi_most_common(current,n):
  '''Return the n most common bigrams that start with current'''
  common = {}
  for k,v in fdist2.items():
     if k[0]==current:
       common[k] = v/len(bi_train)
  top_n = sorted(common, key=common.get, reverse=True)[:n]
  # print(top_n)
  return top_n
def random_uni():
  index = random.randint(0, len(unigrams)-1)
  return unigrams[index]



#generate the sentences
def make_bi_sentance(n):
  probability = 0
  sent = random_uni();
  sent += " "
  while(True):
    n = 50
    if(len(sent.split()) == MAX_LINE_LEN-1):
      break
    choices = bi_most_common(sent.split()[-1], n)
    if(len(choices) == 0):
      next = random_uni()
    elif(len(choices) == 1):
      pair = choices[0]
      next = pair[1]
    elif len(choices) < n:
      n = len(choices)-1
      choice = random.randint(1, n)
      pair = choices[choice]
      next = pair[1]
    else:
      choice = random.randint(1, n-1)
      pair = choices[choice]
      next = pair[1]
    # if len(sent.split()) == 2:
      # probability += math.log2(bi_prob.get(pair))
  #   elif next != '</s>':
  #     probability += math.log2(bi_prob.get(pair))
  #   if next == '</s>' or next == '<s>':
  #     sent += '</s>'
  #     break
    sent += next + " "
  bigram_sentences.append(sent)
  return sent

def print_sentences(sent_list, probability_list):
    for sent,prob in zip(sent_list,probability_list):
        print(f'Probability: {prob}')
        for word in sent.split():
            print(word,end=" ")
        print("\n\n")

def generate_song(f, i):
    # print('\n' + "=" * 30 + "Song " + str(i+1) + "=" * 30, file=f)
    num_stanza = random.randint(2,5)
    for i in range(0, num_stanza):
      num_lines = random.randint(2, 10)
      for j in range(0, num_lines):
        print(make_bi_sentance(35) , file=f)
      print('\n', file=f)
    print("<|end of text|>\n", file=f)  


def main():
  num_songs = int(argv[1])
  for i in range(num_songs):
    with open("bigram_generations.txt","a", encoding='utf-8') as f:
      generate_song(f, i)

if __name__ == '__main__':
  main()




# importing libraries
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('stopwords')
nltk.download('punkt')


with open("paragraphs.txt") as f:

    text = f.read()
text


# Stopwords are common words like "the", "is", "and", etc.
# that are often removed from text cause they usually don't contribute much to the meaning of the text.
stopWords = set(stopwords.words("english"))
# breaks the text into words based on whitespace and punctuation.
words = word_tokenize(text)


freqTable = {}
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1


# Display word frequency count
for word, freq in freqTable.items():
    print(f"{word}: {freq}")

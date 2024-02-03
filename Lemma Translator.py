
#Install Commands (Run these through the command line before executing code)
# pip install nltk
# pip install -U deep-translator
# pip install -U spacy
# python -m spacy download en_core_web_sm (replace variable with desired Spacy model). Download models here: https://spacy.io/models/.  

#nltk related imports
import nltk
nltk.download("stopwords")
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#translator imports
from deep_translator import GoogleTranslator

#for lemmatizing
import spacy

#for input/output handling
import csv

#for punctuation removal
from string import punctuation

#for sorting list of lists
from operator import itemgetter

#Path Variables
input_path = 'test.txt' #must be txt
known_path = 'known_words.csv' #must be csv
output_path = 'test.csv' #must be csv

#Language Variables
stopwords_language = 'italian' #to see list of available languages, run 'print(stopwords.fileids())'
spacy_language_model = 'it_core_news_md' #desired spacy model (installed above)

#Output Header Variables
lemma_header = 'Italian Word'
translation_header = 'English Word'

#opens txt file with string you intend to translate
with open(input_path) as file:
    chapter = file.read()

#opens known words file (csv format) and builds into list
known_words = []
with open(known_path, newline='') as file:
    for row in csv.reader(file):
        known_words.append(row[0])

#use nltk to parse the input string into a list of words
chapter_tokenized = []
chapter_tokenized = word_tokenize(chapter)

#Remove stopwords (words you want to ignore like "in", "is", "an", etc) and punctuation
stop_words = set(stopwords.words(stopwords_language))
punctuation = list(punctuation)

#if you are NOT using a known_words file, comment out / delete "and word.casefold() not in known_words"
stopwords_filtered = []
for word in chapter_tokenized:
    if word.casefold() not in stop_words and word.casefold() not in punctuation and word.casefold() not in known_words:
        stopwords_filtered.append(word)

# Uses map function to set all words in list to lowercase
output = list(map(lambda x:x.lower(), stopwords_filtered))

#Uses Spacy library to load list of lemmatization words
nlp = spacy.load(spacy_language_model)

#creates a list of lemmas based on your previous word list
lemma_list = []
for word in output:
    lemma_list.append(nlp(word)[0].lemma_)

#translates those lemmas using Google Translator
translated_list = []
translated_list = GoogleTranslator('it', 'en').translate_batch(lemma_list)

#creates frequency counts by # of lemmas
dup_list = []
for count, word in enumerate(output):
    num = output.count(word)
    dup_list.append(num)

#creates a 3 column list of lemmas, translations, and frequencies
freq_list = [list(x) for x in zip(lemma_list, translated_list, dup_list)]

#removes duplicates
unique_list = []
[unique_list.append(x) for x in freq_list if x not in unique_list]

#sorts by frequency in descending order and inserts a header row
sorted_list = sorted(unique_list, key=itemgetter(2), reverse=True)
sorted_list.insert(0, [lemma_header, translation_header, "Frequency"])
print(unique_list)

#writes to csv file
with open(output_path, 'w', newline='', encoding="ANSI") as file:
    writer = csv.writer(file)
    writer.writerows(sorted_list)



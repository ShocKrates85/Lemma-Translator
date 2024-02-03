Need support in your language learning journey?

# This Python script does the following:

--Takes in text from a .txt file in a source language of your choice 

--Lemmatizes each word (Lemmatization is the act of taking one form of a word and converting it to its root form.  Example:  'Dogs' become 'dog', 'catches' becomes 'catch', etc)

--Removes any words you already know (as determined by a .csv file which you will point the scipt to.  This file should have a list of words in the first column)

--Translate the lemmas into your desired language

--Output a .csv file with the original lemma, the translated word, and the frequency of occurence

--From there, you can load the .csv file into your favorite flash card app

# Use Case: 
I'm a user looking to read chapter books in a target learning language.  I want to utilize flashcards to help me understand that chapter's vocabulary.  I do NOT want to review flash cards of words I already know.  I need a list of words from the target language, translated in the source language, sorted by frequency that I can load into a flash card app.

# The below variables (embedded in the code) will need updated based on your preferences

## Path Variables
input_path = 'test.txt' #must be txt

known_path = 'known_words.csv' #must be csv

output_path = 'test.csv' #must be csv

## Language Variables
stopwords_language = 'italian' #to see list of available languages, run 'print(stopwords.fileids())'

spacy_language_model = 'it_core_news_md' #desired spacy model (installed above)

## Output Header Variables
lemma_header = 'Italian Word'

translation_header = 'English Word'

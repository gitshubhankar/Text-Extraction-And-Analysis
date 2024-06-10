#Importing the necessary libraries
import requests
from bs4 import BeautifulSoup
import re
import nltk
from textblob import TextBlob

# Downloading  necessary NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Defining the URL of the web page to scrape In my case blackassign0030 from Input excel file
url = "https://insights.blackcoffer.com/what-if-the-creation-is-taking-over-the-creator/"  

# Sending a request to fetch the page content using request & beautiful because static web page
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Locating the title and content 
title = soup.find('h1') # assuming title is h1
article_title = title.get_text(separator=' ', strip=True) if title else "Title not found"

article = soup.find('div', class_='td-post-content tagdiv-type') # Used inpect to check div of article to avoid unnecessary data fetch
article_text = article.get_text(separator=' ', strip=True) if article else "Article content not found"

print("Title:", article_title)
print("Content:", article_text)

# Functions to preprocess the text
def preprocess(text):
    text = text.lower()  # Converts to lowercase
    text = re.sub(r'[^\w\s]', '', text)  # Removes punctuation
    text = re.sub(r'\d+', '', text)  # Removes numbers
    words = text.split()  # Splits into words
    return words

# Preprocessing the article text
words = preprocess(article_text)

# Text analysis functions
def positive_score(text):
    blob = TextBlob(text)
    return sum(1 for sentence in blob.sentences if sentence.sentiment.polarity > 0)

def negative_score(text):
    blob = TextBlob(text)
    return sum(1 for sentence in blob.sentences if sentence.sentiment.polarity < 0)

def polarity_score(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def subjectivity_score(text):
    blob = TextBlob(text)
    return blob.sentiment.subjectivity

def avg_sentence_length(text):
    sentences = nltk.sent_tokenize(text)
    return sum(len(nltk.word_tokenize(sentence)) for sentence in sentences) / len(sentences)

def percentage_complex_words(text):
    words = nltk.word_tokenize(text)
    tagged_words = nltk.pos_tag(words)
    num_complex_words = sum(1 for _, tag in tagged_words if tag in ['JJ', 'RB', 'VBN', 'VBG'])
    return (num_complex_words / len(words)) * 100

def fog_index(text):
    avg_sentence_length_val = avg_sentence_length(text)
    complex_word_percentage = percentage_complex_words(text)
    return 0.4 * (avg_sentence_length_val + complex_word_percentage)

def avg_words_per_sentence(text):
    words = nltk.word_tokenize(text)
    sentences = nltk.sent_tokenize(text)
    return len(words) / len(sentences)

def complex_word_count(text):
    words = nltk.word_tokenize(text)
    tagged_words = nltk.pos_tag(words)
    return sum(1 for _, tag in tagged_words if tag in ['JJ', 'RB', 'VBN', 'VBG'])

def word_count(text):
    words = nltk.word_tokenize(text)
    return len(words)

def syllable_count(word):
    word = word.lower()
    if word.endswith('es'):
        word = word[:-2]
    elif word.endswith('e'):
        word = word[:-1]
    syllables = re.findall(r'[aeiouy]+', word)
    return max(1, len(syllables))

def syllables_per_word(text):
    words = nltk.word_tokenize(text)
    total_syllables = sum(syllable_count(word) for word in words)
    return total_syllables / len(words)

def personal_pronouns(text):
    words = nltk.word_tokenize(text)
    tagged_words = nltk.pos_tag(words)
    return sum(1 for word, tag in tagged_words if tag == 'PRP')

def avg_word_length(text):
    words = nltk.word_tokenize(text)
    return sum(len(word) for word in words) / len(words)

# Perform text analysis for given variables in output excel
positive = positive_score(article_text)
negative = negative_score(article_text)
polarity = polarity_score(article_text)
subjectivity = subjectivity_score(article_text)
avg_sentence_len = avg_sentence_length(article_text)
percent_complex_words = percentage_complex_words(article_text)
fog_index_val = fog_index(article_text)
avg_words_per_sent = avg_words_per_sentence(article_text)
complex_word_count_val = complex_word_count(article_text)
word_count_val = word_count(article_text)
syllables_per_word_val = syllables_per_word(article_text)
personal_pronouns_val = personal_pronouns(article_text)
avg_word_length_val = avg_word_length(article_text)

# Displaying text analysis results
print("\nText Analysis:")
print(f"Positive Score: {positive}")
print(f"Negative Score: {negative}")
print(f"Polarity Score: {polarity}")
print(f"Subjectivity Score: {subjectivity}")
print(f"Avg Sentence Length: {avg_sentence_len}")
print(f"Percentage of Complex Words: {percent_complex_words}")
print(f"FOG Index: {fog_index_val}")
print(f"Avg Words per Sentence: {avg_words_per_sent}")
print(f"Complex Word Count: {complex_word_count_val}")
print(f"Word Count: {word_count_val}")
print(f"Syllables per Word: {syllables_per_word_val}")
print(f"Personal Pronouns: {personal_pronouns_val}")
print(f"Avg Word Length: {avg_word_length_val}")

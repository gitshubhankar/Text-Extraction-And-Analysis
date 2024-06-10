# Text Extraction and Analysis

This project extracts and analyzes text from a specified web page. It performs various text analysis operations, such as calculating sentiment scores, readability indices, and word/sentence metrics.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [Text Analysis Metrics](#text-analysis-metrics)
- [Dependencies](#dependencies)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/gitshubhankar/Text-Extraction-And-Analysis.git
   cd TextExtractionAndAnalysis

Install required libraries
-> pip install -r requirements.txt

## Usage
Ensure you have an active internet connection, as the script fetches content from a specified URL.
Modify the url variable in TextExtractionAndAnalysis.py to the web page you want to analyze.
Run the script:
  python TextExtractionAndAnalysis.py

## Functions

### Text Extraction
title: Extracts the title of the web page.
article_text: Extracts the main content of the web page.

### Preprocessing
preprocess(text): Converts text to lowercase, removes punctuation and numbers, and splits it into words.

### Text Analysis
~ positive_score(text): Calculates the number of positive sentences.
~ negative_score(text): Calculates the number of negative sentences.
~ polarity_score(text): Calculates the overall polarity score.
~ subjectivity_score(text): Calculates the subjectivity score.
~ avg_sentence_length(text): Calculates the average sentence length.
~ percentage_complex_words(text): Calculates the percentage of complex words.
~ fog_index(text): Calculates the FOG index for readability.
~ avg_words_per_sentence(text): Calculates the average number of words per sentence.
~ complex_word_count(text): Counts the number of complex words.
~ word_count(text): Counts the total number of words.
~ syllables_per_word(text): Calculates the average number of syllables per word.
~ personal_pronouns(text): Counts the number of personal pronouns.
~ avg_word_length(text): Calculates the average word length.

### Text Analysis Metrics
Positive Score: Number of positive sentences.
Negative Score: Number of negative sentences.
Polarity Score: Overall polarity (sentiment) of the text.
Subjectivity Score: Degree of subjectivity in the text.
Avg Sentence Length: Average length of sentences in the text.
Percentage of Complex Words: Proportion of complex words in the text.
FOG Index: Readability score indicating the number of years of formal education required to understand the text.
Avg Words per Sentence: Average number of words per sentence.
Complex Word Count: Total number of complex words in the text.
Word Count: Total number of words in the text.
Syllables per Word: Average number of syllables per word.
Personal Pronouns: Number of personal pronouns in the text.
Avg Word Length: Average length of words in the text.

### Dependencies
requests
beautifulsoup4
nltk
textblob

Ensure all dependencies are installed by running:
-> pip install requests beautifulsoup4 nltk textblob


This `README.md` file provides a comprehensive overview of the script, including installation steps, usage instructions, descriptions of the functions and text analysis metrics, and the required dependencies. &#8203;:citation[oaicite:0]{index=0}&#8203;


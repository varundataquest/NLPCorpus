#Natural Language processing (NLP) tests in English
# Operations on NLP Corpus from Univ of Pennsylvania

# Required and setup
# Python 3.10 or greater
# pip2 install nltk
# /Applications/Python\ 3.10/Install\ Certificates.command
# python3 -m nltk.downloader all
# In Pycharm install package nltk in UI



import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

def corpus_info(corpus):
    print(corpus)
    print("README:", corpus.readme())
    files = corpus.fileids()
    print(len(files), "files:")


if __name__ == '__main__':
   corpus_info(nltk.corpus.brown)


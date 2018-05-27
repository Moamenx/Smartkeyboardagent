import nltk
from nltk.tokenize import sent_tokenize
import string
from nltk.util import ngrams
from collections import Counter
from nltk import PorterStemmer, LancasterStemmer, SnowballStemmer
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords

tokenizer = TreebankWordTokenizer()


class NaturalLanguageProcessing():

    def remove_punctuations(self, sentences):

        """Return sentence list with punctuations removed """

        clean_sentences = []
        for text in sentences:
            words = nltk.word_tokenize(text)
            punt_removed = [w for w in words if w.lower() not in string.punctuation]
            word = " ".join(punt_removed)
            clean_sentences.append(word)
        return " ".join(clean_sentences)

    def remove_stopwords(self, sentences, lang='english'):

        """Return the sentence list with stopwords removed"""

        words = nltk.word_tokenize(sentences)
        lang_stopwords = stopwords.words(lang)
        stopwords_removed = [w for w in words if w.lower() not in lang_stopwords]
        return " ".join(stopwords_removed)

    def remove_whitespace(self, sentences):

        """Return the sentence list with whitespaces removed"""

        return " ".join(sentences.split())

    def remove_numbers(self, sentences):

        """Return the sentence list with numbers removed"""

        return nltk.re.sub(r'\d+', '', sentences)

    def words_stemmer(self, sentences, type="SnowballStemmer", lang="english"):

        """Return the sentence list with numbers removed"""

        supported_stemmers = ["PorterStemmer", "LancasterStemmer", "SnowballStemmer"]
        if type is False or type not in supported_stemmers:
            return sentences
        else:
            stem_words = []
        if type == "PorterStemmer":
            stemmer = PorterStemmer()
            for sentence in sentences:
                stem_words.append(stemmer.stem(sentence))
        if type == "LancasterStemmer":
            stemmer = LancasterStemmer()
            for sentence in sentences:
                stem_words.append(stemmer.stem(sentence))
        if type == "SnowballStemmer":
            stemmer = SnowballStemmer(lang)
            for sentence in sentences:
                stem_words.append(stemmer.stem(sentence))

        return " ".join(stem_words)

    def get_ngrams(self, sentences, n):

        """Extracts n-grams from sentences"""

        n_grams = ngrams(nltk.word_tokenize(sentences), n)
        return [' '.join(grams) for grams in n_grams]

    def concatList_to_string(self, words_list):
        return " ".join(words_list)

    def DoTokenizeProcess(self, text):
        # convert text to lowercase ####(optional)###
        text = text.lower()

        # remove numbers from text   ####(optional)###
        text = self.remove_numbers(text)

        sent_tokenize_list = sent_tokenize(text)
        text = self.remove_punctuations(sent_tokenize_list)

        # remove stopwords
        text = self.remove_stopwords(text, lang='english')

        # remove white spaces form text
        text = self.remove_whitespace(text)

        # Porter_text = self.words_stemmer(nltk.word_tokenize(text), "PorterStemmer")
        # Lancaster_text = self.words_stemmer(nltk.word_tokenize(text), "LancasterStemmer")
        Snowball_text = self.words_stemmer(nltk.word_tokenize(text), "SnowballStemmer")
        return Snowball_text
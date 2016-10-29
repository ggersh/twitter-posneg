import re, string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import time

def remove_emoji(data):

    if not data:
        return data
    if not isinstance(data, basestring):
        return data
    try:
    # UCS-4
        patt = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
    except re.error:
    # UCS-2
        patt = re.compile(u'([\u2600-\u27BF])|([\uD83C][\uDF00-\uDFFF])|([\uD83D][\uDC00-\uDE4F])|([\uD83D][\uDE80-\uDEFF])')
    return patt.sub('', data)

def tokenize(tweets):
    words = []
    temp = ""
    i = 0
    for letter in tweets:
        if letter != " " and letter != "." and letter != "!" and letter != "?" and letter != ",":
            temp = temp + letter
        else:
            if len(temp)!= 0:
                words.append(temp)
                temp = ""
    return words


def strip_links(text):
    link_regex    = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    links         = re.findall(link_regex, text)
    for link in links:
        text = text.replace(link[0], ', ')
    return text

def strip_all_entities(text):
    entity_prefixes = ['@','#']
    for separator in  string.punctuation:
        if separator not in entity_prefixes :
            text = text.replace(separator,' ')
    words = []
    for word in text.split():
        word = word.strip()
        if word:
            if word[0] not in entity_prefixes:
                words.append(word)
    return ' '.join(words)

def clean(tweet):
    noLinks = strip_links(tweet)
    noHash = strip_all_entities(noLinks)
    noEmoji1 = remove_emoji(noHash)
    noEmoji = noEmoji1.decode('unicode_escape').encode('ascii','ignore')
    # print noEmoji
    # tokens = tokenize(noEmoji)
    # print tokens
    tokens = sent_tokenize(noEmoji)
    stop_words = set(stopwords.words("english"))
    filtered_sentence = []
    filtered_sentence1 = []
    for i in tokens:
        if i != "RT":
            filtered_sentence.append(i)
    for w in filtered_sentence:
        if w not in stop_words:
            filtered_sentence1.append(w)
    # print filtered_sentence1
    print filtered_sentence1
    return filtered_sentence1

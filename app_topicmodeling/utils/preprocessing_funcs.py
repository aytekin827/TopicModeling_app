from konlpy.tag import Mecab
import string # 특수문자
from gensim import corpora, models
import re


def text_cleaning(docs):
    cleaned_text = []
    # 한국어를 제외한 글자를 제거하는 함수.
    docs = sum(docs, [])
    for doc in docs:
        doc = re.sub("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "", doc)
        cleaned_text.append(doc)

    return cleaned_text

def define_stopwords(path):
    
    SW = set()
    # 불용어를 추가하는 방법 1.
    # 특수문자 불용어 추가
    # string.punctuation = !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
    for i in string.punctuation:
        SW.add(i)

    # 불용어를 추가하는 방법 2.
    # stopwords-ko.txt에 직접 추가
    
    with open(path, encoding='UTF8') as f:
        for word in f:
            SW.add(word)

    return SW

SW = define_stopwords('app_topicmodeling\data\korea_stopwords.txt')

def text_tokenizing(corpus, tokenizer):
    
    mecab = Mecab('C:\mecab\mecab-ko-dic')
    token_corpus = []
    

    if tokenizer == "noun":
        for n in range(len(corpus)):
            token_text = mecab.nouns(corpus[n])
            token_text = [word for word in token_text if word not in SW and len(word) > 1]
                
            token_corpus.append(token_text)
            
    elif tokenizer == "morph":
        for n in range(len(corpus)):
            token_text = mecab.morphs(corpus[n])
            token_text = [word for word in token_text if word not in SW and len(word) > 1]
            token_corpus.append(token_text)

    elif tokenizer == "word":
        for n in range(len(corpus)):
            token_text = corpus[n].split()
            token_text = [word for word in token_text if word not in SW and len(word) > 1]
            token_corpus.append(token_text)
        

    return token_corpus
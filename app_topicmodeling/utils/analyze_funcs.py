from gensim import corpora, models
import pyLDAvis
import pyLDAvis.gensim

def build_doc_term_mat(documents):
    # 문서-단어 행렬 만들어주는 함수.
    print("Building document-term matrix.")
    dictionary = corpora.Dictionary(documents)
    corpus = [dictionary.doc2bow(document) for document in documents]
        
    return corpus, dictionary

def analyze_topic(corpus, dictionary, num_topics,):
    model = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics)
    return model

def print_topic_words(model):
    
    # 토픽 모델링 결과를 출력해 주는 함수.
    print("\nPrinting topic words.\n")
    
    for topic_id in range(model.num_topics):
        topic_word_probs = model.show_topic(topic_id, 10)
        print("Topic ID: {}".format(topic_id))
        
        for topic_word, prob in topic_word_probs:
            print("\t{}\t{}".format(topic_word, prob))
            
        print("\n")

def visualize(model, corpus, dictionary):
    data = pyLDAvis.gensim.prepare(model, corpus, dictionary)
    return data

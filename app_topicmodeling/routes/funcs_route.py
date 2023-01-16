from flask import Blueprint, request, redirect, url_for, Response, render_template, session
from app_topicmodeling.utils.crawling_funcs import crawling_naver_news
from app_topicmodeling.utils.preprocessing_funcs import text_cleaning, text_tokenizing, define_stopwords
from app_topicmodeling.utils.analyze_funcs import build_doc_term_mat, analyze_topic, print_topic_words, visualize
from string import punctuation

bp = Blueprint('funcs', __name__)


@bp.route('/crawling', methods=['POST'])
def news_crawling():
    """
    1. 네이버 api를 이용하여 네이버 뉴스 기사를 크롤링 <<<----
    2. 텍스트 데이터 전처리 text cleaning
    3. tokenizing cleaned_data using Mecab
    4. Modeling
    5. visualization
    """
    # query_str - client로부터 받은 검색어 변수명
    query_str = request.form.get("query_str",None)
    if query_str == '':
        return redirect(url_for('main.index', msg_code=0)+"#about")
    else: 
        # 10번 페이지까지 옮겨가면서 네이버 뉴스를 크롤링한다.
      titles, contents, num_crawled_news = crawling_naver_news(query_str,10)
      
      session['flag'] = 1 # original_flag = 1
      session['titles'] = titles
      session['contents'] = contents
      session['query_str'] = query_str
      session['num_crawled_news'] = num_crawled_news

      print(session['flag'])
      return redirect(url_for('main.index')+"#services")

@bp.route('/clear', methods=['POST'])
def clear_text():
    """
    clear text
    """
    session['flag'] = 0 # cleaned_flag = 2

    return redirect(url_for('main.index')+"#services")

@bp.route('/original', methods=['POST'])
def original_text():
    """
    original text 불러오기
    """
    session['flag'] = 1 # cleaned_flag = 2

    return redirect(url_for('main.index')+"#services")

@bp.route('/preprocessing_cleaning', methods=['POST'])
def access_cleaned_text():
    """
    1. 네이버 api를 이용하여 네이버 뉴스 기사를 크롤링
    2. 텍스트 데이터 전처리 text cleaning <<<----
    3. tokenizing cleaned_data using Mecab
    4. Modeling
    5. visualization
    """
    session['flag'] = 2 # cleaned_flag = 2
    cleaned_text = text_cleaning(session['contents'])
    session['cleaned_text'] = cleaned_text

    return redirect(url_for('main.index')+"#services")

@bp.route('/preprocessing_tokenizing', methods=['POST'])
def access_tokenized_text():
    """
    1. 네이버 api를 이용하여 네이버 뉴스 기사를 크롤링
    2. 텍스트 데이터 전처리 text cleaning 
    3. tokenizing cleaned_data using Mecab <<<----
    4. Modeling
    5. visualization
    """
    session['flag'] = 3 # tokenized_flag = 3
    SW = define_stopwords('app_topicmodeling\data\korea_stopwords.txt')
    tokenized_text = text_tokenizing(session['cleaned_text'],'noun')
    session['tokenized_text'] = tokenized_text

    return redirect(url_for('main.index')+"#services")

@bp.route('/analyze', methods=['POST'])
def analyze():
    """
    1. 네이버 api를 이용하여 네이버 뉴스 기사를 크롤링
    2. 텍스트 데이터 전처리 text cleaning 
    3. tokenizing cleaned_data using Mecab 
    4. Modeling <<<----
    5. visualization
    """

    corpus, dictionary = build_doc_term_mat(session['tokenized_text'])
    model = analyze_topic(corpus, dictionary, 3)

    data = visualize(model,corpus,dictionary)
    print('----'*50)
    print('analyze finished!!!')
    return redirect(url_for('main.index')+"#portfolio")




    
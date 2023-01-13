import urllib.request
import requests
from bs4 import BeautifulSoup 
import pandas as pd
import numpy as np
import time



def crawling_naver_news(query_str, news_page=100):

    # 네이버 개발자 api를 통해 뉴스기사 크롤링
    client_id = "Kd4AD8tY6u5ibXNgOzU6"
    client_secret = "HxVwEez24f"
    encText = urllib.parse.quote(query_str)

    news_data = []
    page_count = news_page

    for idx in range(page_count):
        url = "https://openapi.naver.com/v1/search/news?query=" + encText +"&start=" + str(idx*10+1)

        try:
            result = requests.get(url,
                                headers={"X-Naver-Client-Id":client_id,
                                        "X-Naver-Client-Secret":client_secret}
                                )
            news_data.append(result.json())
        except:
            print("Error Occurred")

    # 네이버 뉴스만 골라내는 과정
    naver_news_link = []
    for page in news_data:

        page_news_link = []

        for item in page['items']:
            link = item['link']
            if 'naver' in link:
                page_news_link.append(link)

        naver_news_link.append(page_news_link)

    # crawling
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

    naver_news_title = []
    naver_news_content = []

    for page, link_page in enumerate(naver_news_link):
        news_page_title = []
        news_page_content = []

        print('====='*20)
        print('page #:',page)
        print('articles for this page:',len(link_page))

        for link in link_page:

            ## 긁어온 URL로 접속하기 ##
            try:
                print(link)
                response = requests.get(link, headers=headers)
                
            except:
                print("ERROR_GET_RESPONSE")
                continue


            ## 뉴스 타이틀 가져오기 ##
            soup = BeautifulSoup(response.text,"html.parser")
            title = None

            try:
                title = soup.find('div',class_='media_end_head_title').get_text().replace('\n', ' ')
            except:
                title = "ERROR_TITLE"

            news_page_title.append(title)
            
            ## 뉴스 본문 가져오기 ##
            doc = None
            text = ""
            
            try:
                content = soup.find('div',class_='go_trans _article_content').get_text().replace('\n', ' ').replace('\t', ' ')
            except:
                content = 'ERROR_CONTENT'
            
            news_page_content.append(content)

            time.sleep(1)

        naver_news_title.append(news_page_title)
        naver_news_content.append(news_page_content)
        
        print('====='*20)
        print()
    
    return naver_news_title, naver_news_content

# # 형태소 분석 들어가기
# mecab = Mecab('C:\mecab\mecab-ko-dic')

from flask import Blueprint, request, redirect, url_for, Response, render_template, session
from app_topicmodeling.utils.crawling_funcs import crawling_naver_news
from app_topicmodeling.utils.preprocessing_funcs import *
from string import punctuation

# from height_app.services 
# from height_app.models import user_model, parents_model, contries_model
# from height_app.utils import main_funcs


bp = Blueprint('modeling', __name__)


@bp.route('/analyze', methods=['POST'])
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
      titles, contents = crawling_naver_news(query_str,1)
      
      session['titles'] = titles
      session['contents'] = contents

      # text cleaning
      # cleaned_contents = text_cleaning(contents)
      # cleaned_titles = text_cleaning(titles)

      # # 불용어 제거
      # SW = set()
      # for i in string.punctuation:
      #       SW.add()
      # with open('app_topicmodeling\data\korea_stopwords.txt',encoding='utf-8') as f:
      #   for word in f:
      #         SW.add()

      # # tokenizing
      # tokenized_text = text_tokenizing(cleaned_contents,'word')
      # print (tokenized_text[0])

      return redirect(url_for('main.index')+"#services")

@bp.route('/preprocessing_cleaining', methods=['POST'])
def preprocessing_cleaning():
    """
    1. 네이버 api를 이용하여 네이버 뉴스 기사를 크롤링
    2. 텍스트 데이터 전처리 text cleaning <<<----
    3. tokenizing cleaned_data using Mecab
    4. Modeling
    5. visualization
    """
    # query_str - client로부터 받은 검색어 변수명
    query_str = request.form.get("query_str",None)
    if query_str == '':
        return redirect(url_for('main.index', msg_code=0)+"#about")
    else: 
      titles, contents = crawling_naver_news(query_str,1)

      print(titles[0], contents[0])

      return redirect(url_for('main.index')+"#services")


# @bp.route('/user', methods=['POST'])
# def add_user():
#     ''' USER PAGE에서 add버튼을 눌렀을때 Post형식으로 넘어온 user 정보를 데이터베이스에 추가(add)하는거 '''

#     userid = user_model.get_users()[-1].id +1 if len(user_model.get_users()) != 0 else 1
#     username = request.form.get('username',None)
#     height = request.form.get('height',None)
#     weight = request.form.get('weight',None)
#     father_height = request.form.get('father_height',None)
#     mother_height = request.form.get('mother_height',None)
#     # sex = request.form.get('sex',None)
#     # birthday = request.form.get('birthday',None)
#     # parent_id = request.form.get('parent_id',None)
#     # country_code = request.form.get('country_code',None)


#     # if username == None:
#     #   return "Needs username",400
#     if height == "":
#       return redirect(url_for('main.user_index', msg_code=5))
#     if weight == "":
#       return redirect(url_for('main.user_index', msg_code=5))
#     if father_height == "":
#       return redirect(url_for('main.user_index', msg_code=5))
#     if mother_height == "":
#       return redirect(url_for('main.user_index', msg_code=5))
#     # if sex == None:
#     #   return "Needs sex",400
#     # if birthday == None:
#     #   return "Needs birthday",400
#     # if parent_id == None:
#     #   return "Needs parent_id",400

#     raw_user = {
#       'id':userid,
#       'username':username,
#       'height':height,
#       'weight':weight,
#       'father_height':father_height,
#       'mother_height':mother_height
#       # 'sex':sex,
#       # 'birthday':birthday,
#       # 'parent_id':parent_id,
#       # 'country_code':country_code
#     }

#     user_model.add_user(raw_user)

#     return redirect(url_for('main.user_index', msg_code=0))


# @bp.route('/user/')
# @bp.route('/user/<int:user_id>')
# def delete_user(user_id=None):
#     """
#     delete_user 함수는 `user_id` 를 엔드포인트 값으로 넘겨주면 해당 아이디 값을 가진 유저를 데이터베이스에서 제거합니다
#     """
#     if user_id == None:
#       return Response(status=400)
    
#     user = user_model.Users.query.filter(user_model.Users.id == user_id).first()
    
#     if not user:
#       return Response(status=404)

#     user_model.delete_user(user_id)

#     return redirect(url_for('main.user_index', msg_code=3))

# @bp.route('/update', methods=['POST'])
# def update_user():
#   '''
#   입력받은 id 의 weight, father_height, mother_height들을 수정하는 함수입니다.
#   '''
#   ID = request.form.get('ID',None)
#   height = request.form.get('height',None)
#   weight = request.form.get('weight',None)
#   father_height = request.form.get('father_height',None)
#   mother_height = request.form.get('mother_height',None)

#   if ID == "":
#     return redirect(url_for('main.update_index', msg_code=5))

#   user_model.update_user(ID,height,weight,father_height,mother_height)

#   return redirect(url_for('main.update_index', msg_code=4))


    
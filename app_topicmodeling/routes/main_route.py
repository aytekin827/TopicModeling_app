from flask import Blueprint, render_template, request,redirect,url_for
from app_topicmodeling.utils.msg_funcs import msg_processor

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    msg_code = request.args.get('msg_code',None)
    alert_msg = msg_processor(msg_code) if msg_code is not None else None


    contents = request.args.get('contents',None)
    return render_template('index.html',alert_msg = alert_msg, contents=contents)



# @bp.route('/#about')
# def predict_index():
#     """
#     예측(predict) 페이지를 보여줍니다.
#     """
#     msg_code = request.args.get('msg_code',None)
#     alert_msg = main_funcs.msg_processor(msg_code) if msg_code is not None else None

#     return render_template('predict_height.html', alert_msg = alert_msg)

# @bp.route('/predict')
# def predict_index():
#     """
#     예측(predict) 페이지를 보여줍니다.
#     """
#     msg_code = request.args.get('msg_code',None)
#     alert_msg = main_funcs.msg_processor(msg_code) if msg_code is not None else None

#     return render_template('predict_height.html', alert_msg = alert_msg)

# @bp.route('/update')
# def update_index():
#     """
#     Post형식으로 데이터가 넘어올경우 키를 수정(update)한 값과 함께 템플릿파일에 넘겨줍니다.
#     """
#     msg_code = request.args.get('msg_code',None)
#     alert_msg = main_funcs.msg_processor(msg_code) if msg_code is not None else None
#     user_list = get_users()

#     return render_template('update.html', alert_msg = alert_msg, user_list=user_list)

# @bp.route('/user')
# def user_index():
#     """
#     user_list 에 유저들을 담아 템플렛 파일에 넘겨줍니다.
#     """

#     # request.args.get함수는 쿼리 스트링을 통해서 넘어온 주소에서 키값을 통해서 value 를 뽑아내준다.
#     msg_code = request.args.get('msg_code', None)

#     alert_msg = main_funcs.msg_processor(msg_code) if msg_code is not None else None

#     user_list = get_users()

#     return render_template('user.html', alert_msg=alert_msg, user_list=user_list)

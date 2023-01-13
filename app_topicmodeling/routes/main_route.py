from flask import Blueprint, render_template, request,redirect,url_for,session
from app_topicmodeling.utils.msg_funcs import msg_processor

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    msg_code = request.args.get('msg_code',None)
    alert_msg = msg_processor(msg_code) if msg_code is not None else None
    
    return render_template('index.html',alert_msg = alert_msg)


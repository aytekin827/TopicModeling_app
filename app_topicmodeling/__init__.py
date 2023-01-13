from flask import Flask, render_template, session
from flask_session import Session


# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__=="__main__":
#     app.run(debug=True)

sess = Session()

def create_app():
    """
    create_app 함수는 어플리케이션 펙토리에 따른 패턴입니다. controller
    """
    app = Flask(__name__)
    sess.init_app(app)

    app.secret_key = '*****'
    app.config['SESSION_TYPE'] = 'filesystem'


    from app_topicmodeling.routes import main_route, funcs_route
    app.register_blueprint(main_route.bp)
    app.register_blueprint(funcs_route.bp, url_prefix='/api')

    return app

if __name__ == '__main__':
    app = create_app()
from flask import flask

def create_app():
    app = Flask(__name)
    '''就是输入name，you initialize
    flask doesn't really matter'''
    app.config['SECRET_KEY'] = 'FDGHK;SDWSLFGA'
    '''乱码字母是密钥，自己设置this is going to
    kind of encrypt or
    secure the cookies and
    session data related to
    our website.'''

    from .views import views
    from .auth import auth

    #注册到flask
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')'''所有URL都存在这个文件里，访问route前都有这个定义的前缀'''
    return app

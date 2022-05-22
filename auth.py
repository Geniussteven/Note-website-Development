from flask import Blueprint

auth = Blueprint('auth', __name__)'''为应用程序设置一个auth蓝图

#接下来定义三个route
@auth.route('/login')
def login():
    return "<p>Login</p>"


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up')
def sign-up():
    return "<p>Sign-up</p>"

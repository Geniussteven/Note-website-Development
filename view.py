from flask import Blueprint

views = Blueprint('views', __name__)'''为应用程序设置一个view蓝图'''

@views.route('/')'''difine the roots'''
def home():'''当进入hit roots 斜线路由，函数就会运行'''
    return"<h1>Test</h1>"'''目的是返回H1的tag-test,当转到slash route,网页上会呈现'''

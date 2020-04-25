from flask import request

from application import app


@app.before_request
def before_request():
    path = request.path
    

#  判断用户是否登录

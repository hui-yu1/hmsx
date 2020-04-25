from flask import Blueprint,render_template,request,jsonify,make_response

from common.models.User import User
from common.libs.user.UserService import UserService
from application import app

import json


router_user = Blueprint('user_page',__name__)

@router_user.route("/login",methods=['POST','GET'])
def login():
    if request.method == 'POST':
        resp = {
            'code':200,
            'msg':'登录成功',
            'data':{}
        }
        req = request.values
        login_name = req['login_name']
        login_pwd = req['login_pwd']
        # 后端校检 不为空 长度不小于1
        if login_name is None or len(login_name) < 1:
            resp['code'] = -1
            resp['msg'] = "请输入正确的用户名"
            return jsonify(resp)
        if login_pwd is None or len(login_pwd) < 1:
            resp['code'] = -1
            resp['msg'] = "请输入正确的密码"
            return jsonify(resp)

        user_info = User.query.filter_by(login_name=login_name).first()
        print(user_info.login_name)
        # 比对用户
        if not user_info:
            resp['code'] = -1
            resp['msg'] = "用户不存在"
            return jsonify(resp)
        # 比对用户状态
        if user_info.status != 1:
            resp['code'] = -1
            resp['msg'] = "账号已被禁用，请联系管理员处理"
            return jsonify(resp)
        # 比对密码
        if user_info.login_pwd != UserService.generatePwd(login_pwd,user_info.login_salt):
            resp['code'] = -1
            resp['msg'] = "密码错误"
            return jsonify(resp)

        # 将用户信息存入到浏览器的Cookie中
        # json.dumps()处理dict，list类型，经过处理后可以直接在浏览器中使用
        response = make_response(json.dumps({'code':200,'msg':'登录成功'}))
        # name vule 过期时间
        # value包括login_name login_pwd login_salt uid
        response.set_cookie(app.config['AUTH_COOKIE_NAME'],'%s@%s'%(UserService.generateAuthCode(user_info),user_info.uid),60*60*24*5)

        return response

        return jsonify(resp)

    return render_template('user/login.html')


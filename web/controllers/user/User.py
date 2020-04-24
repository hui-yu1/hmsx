from flask import Blueprint,render_template,request,jsonify


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
        return jsonify(resp)
    return render_template('user/login.html')


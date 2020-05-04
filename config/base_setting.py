# 设置服务器端口
SERVER_PORT = 8999

# 数据库设置
SQLALCHEMY_DATABASE_URI = 'mysql://root:010205@127.0.0.1/hmsx_db?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# cookie
AUTH_COOKIE_NAME = '1903C_HMSX'

# 拦截器忽略规则
IGNORE_URLS = [
    "^/user/login"
]
IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

STATUS = {
    "1":"正常",
    "0":"已删除"
}
    


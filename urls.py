from application import app
from web.controllers.user.User import router_user

<<<<<<< HEAD
app.register_blueprint(router_user,url_prefix='/user')
=======
app.register_blueprint(router_user, url_prefix='/user')
>>>>>>> 6c785b6... login

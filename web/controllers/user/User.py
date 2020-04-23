<<<<<<< HEAD
from flask import Blueprint
=======
from flask import Blueprint,render_template

>>>>>>> 6c785b6... login

router_user = Blueprint('user_page',__name__)

@router_user.route("/login")
<<<<<<< HEAD
def index():
    return "ok"
=======
def login():
    return render_template('user/login.html')
>>>>>>> 6c785b6... login

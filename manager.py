from application import app,manager
from flask_script import Server
import urls

<<<<<<< HEAD
# web服务器配置
manager.add_command("runserver",Server(host="localhost",port=5000,use_debugger=True,use_reloader=True))
=======
# web 服务器
manager.add_command( "runserver",Server(host="localhost",port=5000,use_debugger=True,use_reloader=True) )
>>>>>>> 6c785b6... login

def main():
    manager.run()

if __name__ == "__main__":
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()
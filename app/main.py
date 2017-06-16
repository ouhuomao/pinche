import import_me 
from flask import Flask
from misc import db_op as dp

my_app = Flask(__name__)

@my_app.route("/")
def hello():
    cursor = dp.get_db(my_app).connect().cursor()
    cursor.execute("SELECT * FROM user")
    res = cursor.fetchall()
    return "welcome to pinche! 3, len: %d"%len(res)

if __name__ == "__main__":
    my_app.run()

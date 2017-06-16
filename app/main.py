import import_me 
from flask import render_template
import jinja2

from misc import db_op as dp
from misc import app_init
    

my_app = app_init.get_app(__name__)

@my_app.route("/main")
def main():
    cursor = dp.get_db(my_app).connect().cursor()
    cursor.execute("SELECT * FROM user")
    res = cursor.fetchall()
    #return "welcome to pinche! 4, len: %d, %s"%(len(res), my_app.config['EXPLAIN_TEMPLATE_LOADING'])
    return render_template('pat/list.pat', test_name="hello this is cy 3")

if __name__ == "__main__":
    my_app.run()

# -*- coding: utf-8 -*-

import import_me 
from flask import render_template
import jinja2
from flask import request

from misc import db_op as dp
from misc import app_init
from misc import constant as cs
from misc.myform import get_form, V_len, V_required, F_str
    

my_app = app_init.get_app(__name__)

@my_app.route("/", methods=["GET", "POST"])
def init():
    form = get_form({
        "appid": F_str("appid", u"微信appid", [V_required(), V_len(max=32)])
    }, request)
    if not form.validate():
        return form.error_msg

    #TODO: use traction here and turn auto-commit to true.
    cursor = dp.get_db(my_app).connect().cursor()
    cursor.execute("select id, name, phone, user_types, msg from user where appid=%s", form.appid.data)
    info = cursor.fetchone()
    if info is None:
        cursor.execute("insert into user(appid, name, phone, user_types, msg, status) values (%s, %s, %s, %s, %s, %s)", \
        (form.appid.data, "", "", "[]", "", cs.USER.STATUS.NORMAL))
    return "init ok"
    

@my_app.route("/main")
def main():
    cursor = dp.get_db(my_app).connect().cursor()
    cursor.execute("SELECT * FROM user")
    res = cursor.fetchall()
    #return "welcome to pinche! 4, len: %d, %s"%(len(res), my_app.config['EXPLAIN_TEMPLATE_LOADING'])
    return render_template('pat/list.pat', test_name="hello this is cy 4")

if __name__ == "__main__":
    my_app.run()

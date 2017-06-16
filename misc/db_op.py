import db_config as dfg
from flaskext.mysql import MySQL


def get_db(app):
    mysql = MySQL()
    app.config.update(dfg.db_fg)
    mysql.init_app(app)
    return mysql



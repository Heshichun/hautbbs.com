import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, config

app = Flask(__name__)
app.config.from_object('config')

def connect_db():
    """一个连接数据库函数。并返回其中的行"""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """创建一个数据库连接"""
    if not hasattr('g' , 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr('g' , 'sqlite_db'):
        g.sqlite_db.close()

if __name__ == '__main__':
    app.run()
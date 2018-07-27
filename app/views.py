import json

import cx_Oracle

from flask import render_template, flash, redirect

from app import app
from app.OraUtil import OracleUtil
from app.forms import LoginForm

db_info = {
    'user': 'SCOTT',
    'pwd': 'abc123',
    'host': '127.0.0.1',
    'port': '1521',
    'sid': 'AkiDemo'
}

ora_util = OracleUtil(db_info)


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Protland!'
         },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers move was so cool!'
        }
    ]
    render = render_template("index.html", title='Home', user=user, posts=posts)
    return render


@app.route('/login', methods=['GET', 'Post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenId="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])


@app.route('/db_test', methods=['GET'])
def db_test():
    columns = ora_util.columns('users')
    return json.dumps(columns)



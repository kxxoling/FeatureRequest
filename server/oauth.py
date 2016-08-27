import logging

from flask import Blueprint
from flask import url_for, redirect, session
from flask_oauthlib.client import OAuth
from flask_login import login_user, logout_user

from .models import User


oauth = Blueprint('oauth', __name__, url_prefix='/oauth')

oauth_client = OAuth()

github = oauth_client.remote_app(
    'github',
    app_key='GITHUB'
)


@github.tokengetter
def get_github_oauth_token():
    return session.get('github_token')


@oauth.route('login')
def github_login():
    return github.authorize(callback=url_for('oauth.github_authorized', _external=True))


@oauth.route('logout')
def logout():
    logout_user()


@oauth.route('login/authorized')
def github_authorized():
    rsp = github.authorized_response()
    if rsp is None:
        logging.info('login failed')
        return
    logging.debug('rsp: ', rsp)
    session['github_token'] = (rsp['access_token'], '')

    data = github.get('user').data
    logging.debug('data: ', data)

    try:
        user = User.query.filter_by(social_id=data['id'])[0]
    except IndexError:
        user = User.create_from_github(data)
        user.save()
    login_user(user)

    return redirect('/admin/user/')

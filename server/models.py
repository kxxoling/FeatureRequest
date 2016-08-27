import datetime

from flask import abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class BasicMixin(object):

    pk = db.Column(db.Integer, primary_key=True)
    time_created = db.Column(db.DateTime,
        default=datetime.datetime.utcnow)          # First time the column is created.
    time_nearest_updated = db.Column(db.DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow)

    @classmethod
    def get_or_404(cls, pk=None, **kwargs):
        if pk is not None:
            obj = cls.query.get(pk)
        else:
            objs = cls.query.filter_by(**kwargs)
            obj = objs and objs[0] or None
        if obj is None:
            abort(404)
        return obj

    def __unicode__(self):
        return "<Model %s>%d: %s" % (self.__class__.__name__, self.pk,
                                     getattr(self, 'name', None) or '')


class SessionMixin(object):
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self


class User(UserMixin, BasicMixin, SessionMixin, db.Model):
    __tablename__ = 'users'

    username = db.Column(db.String(100), unique=False)
    name = db.Column(db.String(100), nullable=False)
    social_id = db.Column(db.String(64), nullable=True)
    avatar = db.Column(db.String(300), nullable=True)

    @classmethod
    def create_from_github(cls, data):
        return cls(
            # email=data['email'],
            username=data['login'],
            social_id=data['id'],
            avatar=data['avatar_url'],
            name=data['name']
        )

    def get_id(self):
        return self.pk


class Feature(BasicMixin, SessionMixin, db.Model):
    __tablename__ = 'features'

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    client = db.Column(db.String(), nullable=False)
    priority = db.Column(db.Integer, nullable=True)
    date = db.Column(db.Date, nullable=True)
    ticket_url = db.Column(db.String(100), nullable=True)
    area = db.Column(db.String(30), nullable=True)

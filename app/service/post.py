# -*- coding: utf-8 -*-

from app.models import Post
from app.extensions import db

class PostService(object):

    @staticmethod
    def add_post(title, content=None):
        post = Post(content=content, title=title)
        db.session.add(post)
        db.session.commit()

        return post.to_dict()


    @staticmethod
    def store_to_db():
        db.session.add()
        db.session.commit()
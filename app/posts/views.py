from flask import render_template

from app.posts import post


from app.models import Post



@post.route('/')
def index():

    posts = Post.query.all()

    return render_template('index.html', posts=posts)


@post.route('/detail/<int:id>')
def detail(id):
    posts = Post.query.get(id)

    return render_template('detail.html', post=posts)
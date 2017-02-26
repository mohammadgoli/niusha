# _*_ coding: utf-8 _*_
from functools import wraps
from flask import flash, redirect, render_template, \
   request, session, url_for, Blueprint
from sqlalchemy.exc import IntegrityError 
from project import app

from .forms import AdminLoginForm
from project import db
from project.models import User, Post, Comment
from werkzeug import secure_filename
import os
#helper functions 
# def blog_post_finder(postTitle):
#     postTitle = u'{}'.format(postTitle)
#     return db.session.query(Post).filter_by(title=postTitle).first()

# def page_number():
#     blog_posts_numbers = db.session.query(Post).count()
#     pageNumber = blog_posts_numbers / 5 
#     if blog_posts_numbers % 5 > 0 :
#         pageNumber += 1 
#     return pageNumber

# def posts(pageNumber):
#     start = ((pageNumber-1)*5) + 1
#     end = (pageNumber*5) + 1
#     return db.session.query(Post).order_by(Post.date.asc())[start:end]

# def comment_search(searchID):
#     return db.session.query(Comment).order_by(Comment.date.asc()).filter_by(Post_ID=searchID)

#This bluePrint includes user registration and users profile system 
upload_blueprint = Blueprint('upload', __name__)

# upload_blueprint.config['UPLOAD_FOLDER'] = 'uploads/'
# # These are the extension that we are accepting to be uploaded
# upload_blueprint.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config["ALLOWED_EXTENSIONS"]
           


@upload_blueprint.route('/testUp')
def testUp():
    return render_template('testUp.html')


@upload_blueprint.route('/upload', methods=['POST'])
def upload():
    error = None
    file_name = request.files['file']

    if file_name and allowed_file(file_name.filename):

        file_name_safe = secure_filename(file_name.filename)

        file_name.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name_safe))

        return redirect(url_for('upload.uploaded_file', filename=file_name_safe))


@upload_blueprint.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

# @admin_blueprint.route('/ad')
# @blog_blueprint.route('/blog/page/<int:pageNumber>')
# def blog(pageNumber):
#     currentPage = pageNumber
#     pages = page_number()
#     if currentPage <= pages:
#         posts_for_specific_page = posts(currentPage)
#     return render_template('blog.html', numbers=pages, posts=posts_for_specific_page)



# @blog_blueprint.route('/blog/post/<postTitle>')
# def blog_post(postTitle):
#     post = postTitle.split("-")
#     postTitle = " ".join(post)
#     post = blog_post_finder(postTitle)
#     comment_id_to_search = post.post_id
#     comments = comment_search(comment_id_to_search)
#     for i in comments:
#         print i.comment
#     return render_template('post2.html', post=post, comments=comments)

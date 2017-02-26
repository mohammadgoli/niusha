# _*_ coding: utf-8 _*_
from functools import wraps
from flask import flash, redirect, render_template, \
   request, session, url_for, Blueprint
from sqlalchemy.exc import IntegrityError 


from .forms import AdminLoginForm
from project import db
from project.models import User, Post, Comment

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
admin_blueprint = Blueprint('admin', __name__)


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap


@admin_blueprint.route('/admin', methods=['GET', 'POST'])
def admin_redirect():
    error = None
    form = AdminLoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            # user = User.query.filter_by(tele_number=request.form['telegram_number']).filter_by(payment_verify=1).first()
            username = "admin"
            password = "test"
            if username is not None and str(username) == str(request.form['username']) and str(password) == str(request.form['password']):
                session['logged_in'] = True
                return redirect(url_for('homepage.main'))
            else:
                "user credentials"
        else:
            print "not validate"
    else:
        print "request.method"

    return render_template('administrator.html', form=form, error=error)


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

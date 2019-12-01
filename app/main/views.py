from flask import render_template,redirect,request,url_for,abort
from . import main
from flask_login import login_required,current_user
from app import db
from app.main import main
# from ..request import get_quotes
from .forms import CommentForm,BlogForm
from ..models import User,Blog,Comment
import datetime
from .. import db,photos

@main.route('/')
# @main.route('/home')
def index():
    '''
    view root page function that returns index and its data 
    '''
    blogs = Blog.query.all()
    return render_template('index.html',blogs=blogs,current_user=current_user)

# @main.route('/blog/<category>')
# def blog(category):
#     '''
#     view root page function that returns index and its data 
#     '''
#     blogs=Blog.get_blogs(category)
#     return render_template('blog.html',blogs=blogs)

@main.route('/blog/new', methods = ['GET','POST'])
@login_required
def new_blog():
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        title = blog_form.title.data
        blog = blog_form.text.data
        category = blog_form.category.data
        
        new_blog = Blog(blog_title=title,blog_content=blog,category=category,user=current_user)
        
        new_blog.save_blog()
        return redirect(url_for('.index'))
    
    title = 'new blog'
    return render_template('new_blog.html',title=title,blog_form=blog_form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
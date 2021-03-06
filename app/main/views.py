from flask import render_template,redirect,request,url_for,abort
from . import main
from flask_login import login_required,current_user
from app import db
from app.main import main
from ..request import get_quotes
from .forms import CommentForm,BlogForm,UpdateProfile
from ..models import User,Blog,Comment
import datetime
from .. import db,photos

@main.route('/')
def index():
    '''
    view root page function that returns index and its data 
    '''
    quotes=get_quotes()
    print(quotes)
    return render_template('index.html',current_user=current_user,quotes=quotes)

@main.route('/blog/<category>')
def blog(category):
    '''
    view root page function that returns index and its data 
    '''
    blogs=Blog.get_blogs(category)
    return render_template('blog.html',blogs=blogs)

@main.route('/blog/new', methods = ['GET','POST'])
@login_required
def new_blog():
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        title = blog_form.title.data
        blog = blog_form.content.data
        category = blog_form.category.data
        
        new_blog = Blog(blog_title=title,blog_content=blog,category=category,user=current_user)
        
        new_blog.save_blog()
        
        return redirect(url_for('.index'))
    
    title = 'new blog'
    return render_template('new_blog.html',title=title,blog_form=blog_form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()
    user_joined = user.date_joined.strftime('%b %d,%Y')
    
    if user is None:
        abort(404)
        return render_template('/profile/profile.html',user = user, date = user_joined)
    
@main.route('/user/<uname>/update', methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()    
    if user is None:
        abort(404)
        
        form = UpdateProfile()
        if form.validate_on_submit():
            user.bio = form.bio.data
            
            db.session.add(user)
            db.session.commit()
            
            return redirect(url_for('.profile',uname=user.username))
            
        return render_template('/profile/update.html', form = form)
        
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

@main.route('/blog/comment/<int:id>', methods = ['GET','POST'])
def comment(id):
    blog = Blog.get_blog(id)
    posted_date = blog.posted.strftime('%b, %d, %Y')
    
    comment_form = CommentForm()
    comments = Comment.get_comments(blog)
    if comment_form.validate_on_submit():
        comment = comment_form.text.data
        
        new_comment = Comment(comment=comment,username=current_user.username,blog_id = blog)
        
        new_comment.save_comment()
        return redirect(url_for("main.comment",id=id))
        
    return render_template('comment.html',comment_form=comment_form,comments=comments)
    
@main.route('/user/<uname>/blogs')
def user_blogs(uname):
    user = User.query.filter_by(username=uname).first()
    blogs = Blog.query.filter_by(user_id = user.id).all()
    user_joined = user.date_joined.strftime('%b %d, %Y')

    return render_template("blog.html", user=user,blogs=blogs,date = user_joined)
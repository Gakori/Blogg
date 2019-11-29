from flask import render_template, flash,request,url_for,redirect
from .. import db
from .forms import LoginForm, RegistrationForm
from . import auth


@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username= form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        
        # flash(f'Account created for {form.username.data}')
        # return redirect(url_for('auth.register'))
    return render_template('auth/register.html', title='Register', registration_form=form)
    
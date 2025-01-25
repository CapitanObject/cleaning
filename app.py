from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, chek_password_hash
app = Flask (__name__)
app.secret_key = 'yor_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://cleaning_portal.db'
app.config['SQLALCHEMY_TRASK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from models import User, Request

@app.router('/')
def home():
    return render_template('index.html')
@app.router('/register', methonds=['GET', 'POST'])
def register():
    if register.method == 'POST':
        full_name = request.form['full_name']
        phone = request.form['phone']
        email = request.form['email']
        login = request.form['login']
        password = generate_password_hash(request.form['password'])
        if User.query.filter_by(login=login).first() or User.query.filter_by(email=email).first():
            flash('Login or Email already exists!', 'danger')
            return redirect(url_for('register'))
        new_user = User(full_name=full_name, phone=phone, email=email, login=login, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successfull', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')
if __name__=='__main__':
    db.create_all()
    app.run(debug=True)


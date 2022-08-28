from flask import Blueprint, render_template, redirect, url_for, request
from .database import connection
from flask_login import login_user, logout_user
from .models import User

  

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
      cursor = connection.cursor()
      login = request.form.get('login')
      query = f"SELECT TOP 1 user_login FROM Tauron_Users WHERE user_login = '{login}'"
      cursor.execute(query)
      row = cursor.fetchone()
      
      if row:
        user = User(login)
        login_user(user)
        cursor.close()
        return(redirect(url_for("main.index")))
      else:
        cursor.close()
        return(redirect(url_for("auth.login")))

    return render_template("login.html", hide_navbar=True)

@auth.route('/logout')
def logout():
    logout_user()
    return(redirect(url_for("auth.login")))
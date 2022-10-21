from flask import Blueprint, render_template, redirect, url_for, request
from .database import connection
from flask_login import login_user, logout_user
from .models import User
import pyodbc


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
      cursor = connection.cursor()
      try:
        login = request.form.get('login')
        password = request.form.get('password')
        query = f"""
        select tu.user_login, tp.user_pass from dbo.Tauron_Users tu
        left join dbo.Tauron_Pass tp on tu.user_id = tp.user_id
        where tu.user_login = '{login}'
        """
        
        cursor.execute(query)
        row = cursor.fetchone()
        connection.commit()
        print(row)
        db_login = row[0]
        db_pass = row[1]
     

        if db_login == login and db_pass == password:
            user = User(login)
            login_user(user)
            return (redirect(url_for("main.index")))
        else:
            return (redirect(url_for("auth.login")))
      except pyodbc.Error as err:
        sqlstate = err.args
        print(sqlstate[1])
        print("Test")
        if sqlstate[0] == '08001':
            return redirect(url_for('main.error', err="Błąd połaczenia z bazą danych"))
        else:
          return redirect(url_for('main.error', err=sqlstate[1]))
        
    return render_template("login.html", hide_navbar=True)


@auth.route('/logout')
def logout():
    logout_user()
    return (redirect(url_for("auth.login")))

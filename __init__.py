#! /var/www/html/Carpenter/Carpenter/env/bin/python3

#imports
from flask import Flask, render_template, url_for
from db import connection

#instansiate Flask object
app = Flask(__name__)


#create view for root url
@app.route('/')
def home():
    #use pymysql cursor
    with connection.cursor() as cursor:
        #select query
        sql = "SELECT * FROM `home_page`"
        cursor.execute(sql,(),)
        result = cursor.fetchall()

    return render_template('home.html',data=result)

@app.route('/gallery/<id>')
def gallery(id):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM gallery_items WHERE title_id = %s"
        cursor.execute(sql,(id),)
        result = cursor.fetchall()
    return render_template('gallery.html',data=result)

if __name__ == '__main__':
    app.run(debug=True)

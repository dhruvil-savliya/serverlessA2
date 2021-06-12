from flask import Flask,render_template,request,session
import mysql.connector
import datetime

app = Flask(__name__)

mydb = mysql.connector.connect(host = "146.148.78.137", user="root", password="ds9898220258", database="db")

mycursor = mydb.cursor()


@app.route('/')
def activeuser():
    # return render_template("afterlogin.html")

    mycursor.execute("select * from user_status where userstatus = '1'")
    data = mycursor.fetchall()

    # print (data)

    return render_template ('afterlogin.html', data = data)


@app.route('/logout', methods= ['POST', 'GET'])
def userlogout():
    em = "dhatu1999@gmail.com"
    mycursor.execute("update user_status SET userstatus = '0' WHERE email = 'dhatu1999@gmail.com' ")
    mydb.commit()

    # return render_template('login.html')

    session.pop('email',None)
    return render_template('http://127.0.0.1:5001/')


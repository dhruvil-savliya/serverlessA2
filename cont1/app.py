from flask import Flask,render_template,request
import mysql.connector
import datetime

app = Flask(__name__)

mydb = mysql.connector.connect(host = "146.148.78.137", user="root", password="ds9898220258", database="db")

mycursor = mydb.cursor()


@app.route('/')
def reg():
    return render_template('register.html')


@app.route('/register', methods= ['POST','GET'])
def reguser():
    
    if request.method == "POST":
        register = request.form
        username = register['username']
        email = register['email'] 
        password = register['password'] 
        topic = register['topic']

        status = '0'
        currenttime = datetime.datetime.now()

        mycursor.execute("insert into user_details (name,email,password,topic) values (%s,%s,%s,%s)",(username,email,password,topic))

        mycursor.execute("insert into user_status (email,userstatus,logintime) values (%s,%s,%s)",(email,status,currenttime))

        mydb.commit()
        mycursor.close()

        return render_template ('successfulreg.html') 
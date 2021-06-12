from flask import Flask,render_template,request,session
import mysql.connector
import datetime

app = Flask(__name__)

mydb = mysql.connector.connect(host = "146.148.78.137", user="root", password="ds9898220258", database="db")

mycursor = mydb.cursor()

@app.route('/')
def signin():
    return render_template('login.html')


@app.route('/loginvalidation', methods = ['POST','GET'])
def loginvalid():
    if request.method == "POST":
        e = request.form.get('mail')
        p = request.form.get('pass')

    mycursor.execute("""SELECT * FROM user_details WHERE email = %s AND password = %s """,(e,p))
    # val=(e,p)
    
    users = mycursor.fetchall()

    if len(users)>0:
        status = '1'

        session['loggedin'] = True
        session['email'] = e
        session['password'] = p
        logintimestamp = datetime.datetime.now()


        mycursor.execute("update user_status set (email,userstatus,logintime) values (%s,%s,%s)",(e,status,logintimestamp))
        mydb.commit();
        return render_template('http://127.0.0.1:5002/')


    # if len(users)>0:
    #     status = '1'
    #     logintimestamp = datetime.datetime.now()
    #     mycursor.execute("insert into user_status (email,userstatus,logintime) values (%s,%s,%s)",(e,status,logintimestamp))
    #     mydb.commit();
    #     return render_template('successlogin.html')
    # else:
    #     return "Fail"
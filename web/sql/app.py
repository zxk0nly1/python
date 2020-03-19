from flask import Flask,request,render_template
import hashlib
import mysql.connector

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')


@app.route('/login',methods=['GET'])
def login_form():
    return render_template('login_form.html')


@app.route('/register',methods=['GET'])
def register_form():
    return render_template('register.html')


@app.route('/login',methods=['POST'])
def login():
    username=request.form['username']
    password=request.form['password']
    md5_password=hashlib.md5()
    md5_password.update(password.encode('utf-8'))

    conn=mysql.connector.connect(user='root',password='',database='dtt_web')
    cursor=conn.cursor()
    cursor.execute(r"select * form user where name ='%s'"%username)
    res=cursor.fetchall()
    cursor.close()
    conn.close()
    if not res[0][0]:
        return render_template('login_form.html',message='用户不存在，请检查后再输入！',username=username)
    elif md5_password.hexdigest() !=res[0][1]:
        return render_template('login_form.html',message='密码错误，请检查后再输入!"',username=username)
    return render_template('login-ok.html',username=username)


@app.route('/register',methods=['POST'])
def register(name=None):
    username=request.form['username']
    password=request.form['password']
    re_password=request.form['re_password']
    md5_password=hashlib.md5()
    md5_password.update(password.encode('utf-8'))
    conn=mysql.connector.connect(user='root',password='',database='dtt_web')
    cursor=conn.cursor()
    cursor.execute(r"select * from user where name = '%s'"%username)
    res=cursor.fetchall()
    if res:
        return render_template('register.html',message='用户名已存在，请直接登录！',username=username)
    elif password!=re_password:
        return render_template('register.html',message='两次输入的密码不一致，请检查后再输入！',username=username)
    elif not username or not password:
        return render_template('register.html',message='用户名和密码不能为空，请检查后再输入！',username=username)

    cursor.execute('insert into user(name,password) values (%s,%s)',[username,md5_password.hexdigest()])
    conn.commit()
    cursor.close()
    return render_template('register-ok.html')


if __name__=='__main__':
    # 若不配置host和port，则默认是localhost，端口为5000
    app.run("",8000)
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html", alertIt=False)

@app.route("/signUpPage")
def signUpPage():
    return render_template("signUp.html")

@app.route("/login", methods=["POST"])
def login():
    conn = sqlite3.connect("userDB.db")
    cur = conn.cursor()
    
    ID = request.form['ID']
    PW = request.form['PW']
    
    result = list(cur.execute("select * from user_info where ID = \"" + ID + "\""))

    conn.close()

    if result:
        if PW == result[0][1]:
            return "로그인 성공!"
        else:
            return render_template("login.html", alertIt=True)
    else:
        return render_template("login.html", alertIt=True)

@app.route("/signUp", methods=["POST"])
def signUp():
    conn = sqlite3.connect("userDB.db")
    cur = conn.cursor()
    
    ID = request.form['ID']
    PW = request.form['PW']

    result = list(cur.execute("select * from user_info where ID = \"" + ID + "\""))

    if result:
        conn.close()
        return render_template("signUp.html", alertIt=True, comment="중복된 아이디가 있습니다.")
    
    else:
        cur.execute("insert into user_info values('%s', '%s')"%(ID, PW))
        conn.commit()

        conn.close()
        print(ID, PW, "생성")
        return "회원가입 성공! <a href=\"../../\">로그인 하러 가기</a>"
    
app.run()

from flask import *
from blogdb import *

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/RegAut')
def RegAut():
    return render_template("RegAut.html")

@app.route('/RegUser')
def RegUser():
    return render_template("RegUser.html")

@app.route('/LogAuth')
def LogAuth():
    return render_template("LogAuth.html")

@app.route('/LogUser')
def LogUser():
    return render_template("LogUser.html")

@app.route('/AuthInt')
def AuthInt():
    return render_template("AuthInt.html")

@app.route('/AddPost')
def AddPost():
    return render_template("AddPost.html")

@app.route("/RegA",methods=["post"])
def add_Author():
    
    name=request.form["uName"]
    passw=request.form["uPass"]
    email=request.form["uMail"]
    city=request.form["uCity"]
    t=(None,name,passw,city,email)
    InsertAuth(t)
    return redirect("/")

@app.route("/RegU",methods=["post"])
def add_User():
    
    name=request.form["uName"]
    passw=request.form["uPass"]
    email=request.form["uMail"]
    city=request.form["uCity"]
    t=(None,name,passw,city,email)
    InsertUser(t)
    return redirect("/")

@app.route("/AllPost")
def All_Post():
    data1=selectAllPost()
    return render_template("AllPost.html",plist=data1)

@app.route("/LogU",methods=["post"])
def LogU():
    name=request.form["uName"]
    passw=request.form["uPass"]
    t=name
    Log_User(t)
    data=Log_User(t)
    if name==data[0][0] and passw==data[0][-1]:
        return redirect("/AllPost")
    else:
        return redirect("LogUser.html")

@app.route("/LogA",methods=["post"])
def LogA():
    name=request.form["uName"]
    
    passw=request.form["uPass"]
    
    global x
    x=request.form["uName"]
    
    t=name
    Log_Auth(t)
    data=Log_Auth(t)
   
    
    if name==data[0][0] and passw==data[0][-1]:
        
        return redirect("/AuthInt")
    else:
        return redirect("/")



@app.route("/intB",methods=["post"])
def add_Blog():
    
    name=request.form["uName"]
    title=request.form["uTitle"]
    blog=request.form["Blog"]
    t=(None,name,title,blog)
    InsertPost(t)
    
    return redirect("/AuthInt")

@app.route("/YouPost")
def YouPost():
    n1=x
    selectAPost(n1)
    data1=selectAPost(n1)
    
    return render_template("YouPost.html",pl=data1)
    
    




    

if __name__=="__main__":
    app.run(debug=True)

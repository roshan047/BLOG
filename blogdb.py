import pymysql as p

def connect():
    return p.connect(host="localhost",user="root",password="",database="blog")
def InsertAuth(t):
    db=connect()
    sql="insert into author values(%s,%s,%s,%s,%s)"
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def InsertUser(t):
    db=connect()
    sql="insert into user values(%s,%s,%s,%s,%s)"
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def Log_User(t):
    db=connect()
    sql="select  U_UNAME,U_PASSWORD from user where  U_UNAME=%s"
    cr=db.cursor()
    cr.execute(sql,t)
    Ulist=cr.fetchall()
    db.commit()
    db.close()
    return Ulist

def Log_Auth(t):
    db=connect()
    sql="select  A_UNAME,A_PASSWORD from author where A_UNAME=%s"
    cr=db.cursor()
    cr.execute(sql,t)
    Ulist=cr.fetchall()
    db.commit()
    db.close()
    return Ulist

def InsertPost(t):
    db=connect()
    
    sql1="insert into author_post values(%s,%s,%s,%s)"
    cr=db.cursor()
    cr.execute(sql1,t)
    db.commit()
    db.close()

def selectAllPost():
    db=connect()
    sql='select * from author_post'
    cr=db.cursor()
    cr.execute(sql)
    Alist=cr.fetchall()
    db.commit()
    db.close()
    return Alist

def selectAPost(n):
    db=connect()
    sql='select * from author_post where P_UNAME=%s'
    cr=db.cursor()
    cr.execute(sql,n)
    Alist=cr.fetchall()
    db.commit()
    db.close()
    return Alist

##def name(n):
##    db=connect()
##    cur=db.cursor()
##    sql="select * from 
















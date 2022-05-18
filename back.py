import sqlite3


def connect():
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT ,author TEXT, year ineteger,isdn integer)")
    conn.commit()
    conn.close()



def insert(title,author,year,isdn):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor() 
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isdn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("book.db")
    cur=conn.cursor() 
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows


def search(title="",author="",year="",isdn=""):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor() 
    cur.execute("SELECT * FROM book WHERE title=? or author=? or year=? or isdn=?",(title,author,year,isdn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor() 
    cur.execute("DELETE FROM  book WHERE id=?",(id,))
    conn.commit()
    conn.close()
    

def update(id,title,author,year,isdn):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor() 
    cur.execute("UPDATE  book SET title=?,author=?,year=?,isdn=? WHERE id=?",(id,title,author,year,isdn))
    conn.commit()
    conn.close()


connect()
#insert("the","neelam malik",2010,123456789)
#delete(3)
#update(4,"the moon","hunavi",2014,233)
#print(view())
#print(search(author="neelam malik"))


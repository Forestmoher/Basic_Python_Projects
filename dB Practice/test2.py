import sqlite3

filelist = ('infomation.docx','hello.txt','myImage.png','myMovie.mpg', \
            'world.txt','data.pdf','myphoto.pdf')

conn = sqlite3.connect("test2.db")

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_textfiles(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect("test2.db")

for  x in filelist:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_textfiles(col_fname) VALUES (?)",(x,))
            conn.commit()
            print(x)
conn.close()

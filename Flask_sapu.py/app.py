from flask import Flask,render_template,request,redirect,url_for
import sqlite3
import traceback

app = Flask(__name__)

@app.route('/')
def index():   
    dbpath = 'BOOK.db'
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    
    #テーブルの作成
    sql="CREATE TABLE IF NOT EXISTS books(title TEXT,price INTEGER,arrival_day TEXT)"
    cur.execute(sql)

    #データの取得
    sql="SELECT * FROM books"
    cur.execute(sql)
    conn.commit()

    result=cur.fetchall()
    cur.close()
    conn.close()

    books=[]
    for row in result:
        books.append({'title':row[0],'price':row[1],'arrival_day':row[2]}) #appendでリストに追加

    return render_template('index.html',books=books)


@app.route('/form')
def form():
    return render_template('form.html')


#登録
@app.route('/register',methods=['POST'])
def register():
    title=request.form['title']
    price=request.form['price']
    arrival_day=request.form['arrival_day']

    dbpath = 'BOOK.db'
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    #データの挿入
    sql="INSERT INTO books VALUES(?,?,?)"
    cur.execute(sql,[title,price,arrival_day])

    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

#削除
@app.route('/delete/<int:book_id>', methods=['POST']) #<int:book_id>でbook_idをint型で受け取る
def delete(book_id):
    dbpath = 'BOOK.db'
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    #データの削除
    sql = "DELETE FROM books WHERE rowid = ?"
    cur.execute(sql, (book_id,))

    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for('index'))

#編集
@app.route('/edit/<int:book_id>', methods=['GET','POST'])
def edit(book_id):
    try:
        title=request.form['title'] #request.formでformから送られたデータを受け取る
        price=request.form['price']
        arrival_day=request.form['arrival_day']
        
        dbpath = 'BOOK.db'
        conn = sqlite3.connect(dbpath)
        cur = conn.cursor()

        #データの更新
        sql="UPDATE books SET title=?,price=?,arrival_day=? WHERE rowid=?"
        cur.execute(sql,(book_id,))

        conn.commit()
        cur.close()
        conn.close()

        return render_template('edit.html',title=title,price=price,arrival_day=arrival_day)
    except:
        print("エラーが発生しました")

if __name__ == "__main__":
    app.run(debug=True,port=5002)
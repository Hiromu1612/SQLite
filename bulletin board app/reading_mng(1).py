import PySimpleGUI as sg
from datetime import timedelta,datetime
import sqlite3

conn=sqlite3.connect('Books.db')
cur=conn.cursor()
print("データベースに接続完了")

today=datetime.now()
date_list = [(today + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(-365, 365)]
theme=sg.theme("GrayGrayGray")

layout=[[sg.Text("読書管理アプリ",size=(30,1),font=(None,20),justification="right")],
        [sg.Push(),sg.Button("追加",key="add_btn"),sg.Push(),sg.Button("更新",key="update_btn"),sg.Push(),sg.Button("削除",key="delete_btn"),sg.Push()],
        #[sg.Frame("読書リスト",[[sg.Listbox(values=[],size=(100,60),key="list")]])]] #size=(横,縦)
        #auto_size_columns:Trueで列の幅を自動調整
        [sg.Table(values=[["","","","","","","","","","",""]],
                headings=["#","タイトル","著者","評価","ステータス","購入日","開始日","終了日","ページ数","URL","コメント"],auto_size_columns=False,justification="left",key="table")]]

window=sg.Window("読書アプリ",layout,size=(700,500))

#データベースから情報を取得
sql="SELECT * FROM books" 
cur.execute(sql)
result = cur.fetchall()
print(result)

# Windowのテーブルにデータを表示
window["table"].update(values=result)



def add():
    # サブウィンドウの作成
    layout = [[sg.Text("タイトル", size=(7, 1)), sg.InputText(key="title"),        sg.Text("著者", size=(4, 1)), sg.InputText(key="author")],
            [sg.Text("評価", size=(4, 1)), sg.Combo(("A","B","C","D"),key="evaluation",default_value="A"),         sg.Text("ステータス", size=(9, 1)), sg.Combo(("未読","読書中","読了"),key="status",size=(10,1),default_value="未読")],
            [sg.Text("購入日", size=(6, 1)), sg.Combo(date_list,key="purchase_date", default_value=today.strftime('%Y-%m-%d')),    sg.Text("開始日", size=(6, 1)),sg.Combo(date_list,key="start_date", default_value=today.strftime('%Y-%m-%d'))],
            [sg.Text("終了日", size=(6, 1)), sg.Spin(values=date_list,key="end_date",initial_value=today.strftime('%Y-%m-%d')),         sg.Text("総ページ数", size=(9, 1)), sg.InputText(size=(5,1),key="page_count")],
            [sg.Text("URL",size=(5,1)),sg.InputText(key="url")],
            [sg.Text("コメント", size=(7, 1)), sg.InputText(key="comment", size=(100, 100))],
            [sg.Button("追加", key="add_btn2"),                                     sg.Button("キャンセル", key="cancel_btn")]]
    
    sub_window = sg.Window("書籍の追加", layout,size=(900,500),resizable=True)

    while True:
        event, values = sub_window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "entry_btn":
            # テーブルに値を追加
            row = [str(len(window["table"].get()) + 1)] + [values[key] for key in ["title", "author", "evaluation", "status", "purchase_date"]]
            window["table"].update(values=[*window["table"].get(), row])
            print("登録ボタンが押されました")
        if event == "cancel_btn":
            break
    sub_window.close()

def update():
    print("更新ボタンが押されました")
def delete():
    if event=="delete_btn":
        delete_choice=sg.popup_yes_no("削除しますか？")
        if delete_choice=="Yes":
            window["table"].delete(values=window["table"].get())
    print("削除ボタンが押されました")

while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED:
        cur.close()
        conn.close()
        print("データベースの接続終了")
        break
    if event=="add_btn":
        add()
    if event=="update_btn":
        update()
    if event=="delete_btn":
        delete()

window.close()
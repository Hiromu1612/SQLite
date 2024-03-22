#tkinterを使って読書管理アプリを作成する
#tkinterをtkとしてインポート
#ttkは見た目をリッチにするためのモジュール
#messageboxはメッセージボックスを表示するためのモジュール
#tkcalendarはカレンダー入力を可能にするためのモジュール
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("読書アプリ")


if __name__ == "__main__":
    #ウィンドウを作成
    #mainloop()でアクションを待ち受ける
    root = tk.Tk()
    mainWindow = MainWindow(master=root)
    mainWindow.mainloop()
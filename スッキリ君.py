import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil
import re


def find_file(filepath, dst_dir, counter=0):
    disable_button()
    # メッセージボックスを表示する時に用いる変数
    counter += 1
    for dir in os.listdir(filepath):
        path = os.path.join(filepath, dir)
        if os.path.isdir(path):
            find_file(path, dst_dir, counter)
        else:
            XXXXXX = os.path.splitext(os.path.basename(path))[0]
            jpeg = os.path.splitext(os.path.basename(path))[1]
            split = re.split("/|\\\\", path)
            ss = split[-2]
            mm = split[-3]
            try:
                hh = int(split[-4])
            except ValueError:
                break
            except IndexError:
                break
            dd = split[-5]
            MM = split[-6]
            yyyy = split[-7]
            if hh < 15:
                hh += 9
            else:
                dd = int(dd)
                hh += 9 - 24
                dd += 1
                if dd < 10:
                    dd = "0{0}".format(dd)
            if hh < 10:
                hh = "0{0}".format(hh)
            shutil.copy(path, dst_dir+"\\{0}{1}{2}{3}{4}{5}_{6}{7}"
                        .format(yyyy, MM, dd, hh, mm, ss, XXXXXX, jpeg))
    if counter == 1:
        able_button()
        messagebox.showinfo("お知らせ", "ファイルを移動しました！")


# 決定ボタンの有効化
def able_button():
    try:
        if target and dest:
            decision_button["state"] = "normal"
    except NameError:
        print("")


# 決定ボタンの無効化
def disable_button():
    if decision_button["state"] == "normal":
        decision_button["state"] = "disable"


# フォルダの参照処理
def click_refer_button():
    dir = 'C:\\pg'
    fld = filedialog.askdirectory(initialdir=dir)
    return fld


def click_refer_button1():
    global target
    target = click_refer_button()
    fld_path1.set(target)
    able_button()


def click_refer_button2():
    global dest
    dest = click_refer_button()
    fld_path2.set(dest)
    able_button()


if __name__ == '__main__':
    # ウィンドウを作成
    root = tkinter.Tk()
    root.title(u"スッキリくん")  # アプリの名前
    root.geometry("500x300")  # アプリの画面サイズ

    # Frame1の作成
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    # 「フォルダ」ラベルの作成
    s = StringVar()
    s.set('フォルダ：')
    label1 = ttk.Label(frame1, textvariable=s)
    label1.grid(row=1, column=0)

    # 「保存先フォルダ」ラベルの作成
    w = StringVar()
    w.set("保存先フォルダ：")
    label2 = ttk.Label(frame1, textvariable=w)
    label2.grid(row=2, column=0)

    # 参照ファイルのパスを表示するテキストボックスの作成
    fld_path1 = StringVar()
    filepath_entry1 = ttk.Entry(frame1, textvariable=fld_path1, width=50)
    filepath_entry1.grid(row=1, column=1)

    # 保存先フォルダのパスを表示するテキストボックスの作成
    fld_path2 = StringVar()
    filepath_entry2 = ttk.Entry(frame1, textvariable=fld_path2, width=50)
    filepath_entry2.grid(row=2, column=1, pady=50)

    # 参照ボタン1の作成
    refer_button1 = ttk.Button(root, text=u'参照', command=click_refer_button1)
    refer_button1.place(x=410, y=8)

    # 参照ボタン2の作成
    refer_button2 = ttk.Button(root, text=u"参照", command=click_refer_button2)
    refer_button2.place(x=410, y=78)

    style = ttk.Style()
    style.configure("BW.TLabel", foreground="#ffffff", background="#cd5c5c",
                    width=15, height=13, anchor='center')

    # 決定ボタンの作成
    decision_button = ttk.Button(root, text=u"決定", style="BW.TLabel",
                                 state="disabled",command=lambda:
                                 find_file(target, dest, counter=0))
    decision_button.place(x=350, y=150)

    # ツールを起動
    root.mainloop()
